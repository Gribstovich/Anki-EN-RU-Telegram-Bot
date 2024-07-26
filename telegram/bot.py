import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import config
from filters.exclude_start_filter import ExcludeStartFilter
from filters.user_filter import UserFilter
from handlers.register_handlers import register_all_handlers

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Bot and Dispatcher
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

# Initialize and apply filters
user_filter = UserFilter()
exclude_start_filter = ExcludeStartFilter(user_filter)
dp.message.filter(exclude_start_filter)

# Register handlers
register_all_handlers(dp)


async def on_startup() -> None:
    """
    Set bot commands when the bot starts up.
    """
    await bot.set_my_commands([
        BotCommand(command='/start', description='Запустить бота'),
        BotCommand(command='/help', description='Помощь')
    ])


if __name__ == '__main__':
    dp.startup.register(on_startup)
    dp.run_polling(bot)
