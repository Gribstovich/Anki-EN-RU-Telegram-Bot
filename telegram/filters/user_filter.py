from aiogram import types
from aiogram.filters import BaseFilter

from telegram.config import config


class UserFilter(BaseFilter):
    """
    Filter to check if the user is allowed to use the bot.
    """

    async def __call__(self, message: types.Message) -> bool:
        """
        Determine if the user is in the list of allowed users.

        :param message: The message object from the user.
        :return: True if the user is allowed, False otherwise.
        """
        return message.from_user.id in config.ALLOWED_USER_IDS
