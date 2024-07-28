from aiogram import Dispatcher, F, types
from aiogram.filters.callback_data import CallbackQuery

from anki import anki_api
from telegram.config import config
from telegram.keyboards.deck_keyboard import generate_deck_keyboard
from wooordhunt import parser

word = None


async def handle_text_message(message: types.Message) -> None:
    """
    Handles text messages from users.

    This function processes messages to check if they contain a single English word.
    If the message does not contain a valid English word, it sends a response indicating
    that the message does not contain an English word. If the word is valid, it retrieves
    its details and sends a formatted reply with the word's information and an inline
    keyboard for deck selection.

    :param message: The message object containing the text message from the user.
    """
    text = message.text
    if not (text.isalpha() and text.isascii() and len(text.split()) == 1):
        await message.reply(config.NOT_ENGLISH_WORD_MESSAGE.format(message.from_user.id))
        return

    global word
    word = await parser.get_word(text)
    if not word or not any((word.description, word.transcription, word.rank, word.examples)):
        await message.reply('WooordHunt не знает такого слова')
    else:
        if word.examples:
            examples = '\n———\n'.join([f'{e[0]}\n{e[1]}' for e in word.examples][:5])
        else:
            examples = None
        text = (f'<a href="https://wooordhunt.ru/word/{word.name}">{word.name}</a>\n\n'
                f'<strong>Перевод:</strong> {word.description}\n'
                f'<strong>Транскрипция:</strong> {word.transcription}\n'
                f'<strong>Популярность:</strong> {word.rank}\n\n'
                f'<strong>Примеры:</strong>\n'
                f'{examples}')
        if all((word.name, word.description, word.transcription)):
            await message.reply(text, reply_markup=await generate_deck_keyboard())
        else:
            text += '\n\n<strong>Невозможно сохранить слово из-за отсутствия названия, перевода или транскрипции</strong>'
            await message.reply(text)


async def handle_deck_selection(callback_query: CallbackQuery) -> None:
    """
    Handles deck selection from the inline keyboard.

    This function processes the callback query to determine the selected deck based
    on the callback data. It then adds the word to the selected deck, synchronizes
    with Anki, and sends a confirmation message.

    :param callback_query: The callback query object containing the callback data from the inline keyboard.
    """
    await callback_query.message.edit_text(callback_query.message.html_text)

    deck = callback_query.data
    if deck == "Don`t_Save":
        await callback_query.message.reply('Сохранение отменено')
    else:
        global word
        await anki_api.add_note(deck,
                                front=f'{word.name}<br>{word.transcription}',
                                back=word.description)
        await anki_api.sync()
        await callback_query.message.reply(f'Слово сохранено в колоду: {deck}')
    await callback_query.answer()


def register_query_handlers(dp: Dispatcher) -> None:
    """
    Register query handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    dp.message.register(handle_text_message, F.text)
    dp.callback_query.register(handle_deck_selection)
