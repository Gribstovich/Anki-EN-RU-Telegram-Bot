from aiogram import F
from aiogram import types, Dispatcher
from aiogram.enums import ParseMode

from telegram.config import config


async def handle_text_message(message: types.Message) -> None:
    """
    Handle all other text messages.

    This handler checks if the message contains only one English word.
    If the message does not meet this criterion, it sends a response indicating
    that the message is not an English word.

    :param message: The message object containing the text message.
    """
    text = message.text
    # Check if the text contains only one English word
    if not (text.isalpha() and text.isascii() and len(text.split()) == 1):
        await message.reply(
            config.NOT_ENGLISH_WORD_MESSAGE.format(message.from_user.id),
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    await message.reply(text)


def register_query_handlers(dp: Dispatcher) -> None:
    """
    Register query handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    dp.message.register(handle_text_message, F.text)
