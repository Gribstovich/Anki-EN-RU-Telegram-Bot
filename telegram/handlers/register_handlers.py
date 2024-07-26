from aiogram import Dispatcher

from .query import register_query_handlers
from .start_command import register_start_command_handler


def register_all_handlers(dp: Dispatcher) -> None:
    """
    Register all handlers with the dispatcher.

    :param dp: The dispatcher instance to register handlers with.
    """
    register_start_command_handler(dp)
    register_query_handlers(dp)
