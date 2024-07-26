import os

from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        """
        Load environment variables from a .env file.
        """
        load_dotenv()
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')
        self.ALLOWED_USER_IDS = list(map(int, os.getenv('ALLOWED_USER_IDS').split(',')))

        self.USER_NOT_AUTHORIZED_MESSAGE = """*У вас нет доступа к боту\.*\n
Чтобы получить доступ, откройте файл `telegram\\\\\.env` и добавьте следующую строку: `ALLOWED_USER_IDS={}`\.\n
Если вы пользуетесь ботом с нескольких аккаунтов, добавьте их id через запятую\."""

        self.HELP_MESSAGE = """Напишу позднее"""

        self.NOT_ENGLISH_WORD_MESSAGE = """Бот понимает только сообщения из одного слова латинскими буквами\."""


config = Config()
