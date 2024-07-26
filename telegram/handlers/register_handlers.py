from aiogram import Dispatcher

from .commands import register_command_handlers
from .query import register_query_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    """
    Register all handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    register_command_handlers(dp)
    register_query_handlers(dp)
