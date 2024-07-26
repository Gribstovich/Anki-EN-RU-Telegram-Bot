from aiogram import types
from aiogram.filters import BaseFilter

from .user_filter import UserFilter


class ExcludeStartFilter(BaseFilter):
    """
    Filter to exclude the /start command from being filtered by UserFilter.
    """

    def __init__(self, user_filter: UserFilter):
        """
        Initialize the ExcludeStartFilter.

        :param user_filter: An instance of UserFilter to apply to non-/start commands.
        """
        self.user_filter = user_filter

    async def __call__(self, message: types.Message) -> bool:
        """
        Allow /start command and apply UserFilter to other messages.

        :param message: The message object from the user.
        :return: True if the message is /start or passes the UserFilter, False otherwise.
        """
        if message.text and message.text.startswith('/start'):
            return True
        return await self.user_filter.__call__(message)
