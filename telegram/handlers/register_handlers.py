from aiogram import Dispatcher

from .commands import register_command_handlers


def register_all_handlers(dp: Dispatcher):
    register_command_handlers(dp)
