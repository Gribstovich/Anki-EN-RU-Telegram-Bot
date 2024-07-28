from aiogram import types, Dispatcher
from aiogram.filters import Command

from telegram.config import config


async def start_command(message: types.Message) -> None:
    """
    Handle the /start command.

    :param message: The message object containing the /start command.
    """
    if message.from_user.id not in config.ALLOWED_USER_IDS:
        await message.answer(config.USER_NOT_AUTHORIZED_MESSAGE.format(message.from_user.id))
        return
    await message.answer(config.START_MESSAGE)


def register_start_command_handler(dp: Dispatcher) -> None:
    """
    Register command handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    dp.message.register(start_command, Command(commands='start'))
