from aiogram import types, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command

from telegram.config import config


async def start_command(message: types.Message) -> None:
    """
    Handle the /start command.

    :param message: The message object containing the /start command.
    """
    if message.from_user.id not in config.ALLOWED_USER_IDS:
        await message.answer(
            config.USER_NOT_AUTHORIZED_MESSAGE.format(message.from_user.id),
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    await message.answer(config.HELP_MESSAGE)


async def help_command(message: types.Message) -> None:
    """
    Handle the /help command.

    :param message: The message object containing the /help command.
    """
    await message.answer(config.HELP_MESSAGE)


def register_command_handlers(dp: Dispatcher) -> None:
    """
    Register command handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    dp.message.register(start_command, Command(commands='start'))
    dp.message.register(help_command, Command(commands='help'))
