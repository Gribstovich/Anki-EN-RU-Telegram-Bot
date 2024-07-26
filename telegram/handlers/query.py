from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackQuery

from anki import anki_api
from telegram.config import config
from telegram.keyboards.deck_keyboard import generate_deck_keyboard


async def handle_text_message(message: types.Message) -> None:
    """
    Handle all other text messages.

    This handler checks if the message contains only one English word.
    If the message does not meet this criterion, it sends a response indicating
    that the message is not an English word.

    :param message: The message object containing the text message.
    """
    text = message.text
    if not (text.isalpha() and text.isascii() and len(text.split()) == 1):
        await message.reply(
            config.NOT_ENGLISH_WORD_MESSAGE.format(message.from_user.id),
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    # text = wooordhunt_data
    await message.reply('В какую колоду сохранить?', reply_markup=await generate_deck_keyboard())


async def handle_deck_selection(callback_query: CallbackQuery) -> None:
    """
    Handle inline keyboard button presses.

    This handler will be called when the user presses a button on the inline keyboard.
    It checks the callback data to determine which deck was selected and sends a response.

    :param callback_query: The callback query object containing the callback data.
    """

    await callback_query.message.edit_text(callback_query.message.text)

    deck = callback_query.data
    if deck == "Don`t_Save":
        await callback_query.message.reply('Сохранение отменено')
    else:
        await anki_api.add_note(deck, front='', back='')
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
