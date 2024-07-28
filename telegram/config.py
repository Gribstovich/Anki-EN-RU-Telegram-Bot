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
        self.USER_NOT_AUTHORIZED_MESSAGE = """<strong>У вас нет доступа к боту</strong>\n\nОткройте файл <code>telegram\\.env</code> и добавьте свой user id (<code>{}</code>) в переменную <code>ALLOWED_USER_IDS</code>\n\nЕсли вы пользуетесь ботом с нескольких аккаунтов, добавьте их id через запятую\n\nПодробности в <a href="https://github.com/Gribstovich/WooordHunt-to-Anki-Bot">репозитории</a> проекта"""
        self.START_MESSAGE = """Отправьте английское слово, бот найдёт его в WooordHunt и предложит сохранить в вашу коллекцию в Anki\n\nПодробности в <a href="https://github.com/Gribstovich/WooordHunt-to-Anki-Bot">репозитории</a> проекта"""
        self.NOT_ENGLISH_WORD_MESSAGE = """Бот понимает только сообщения из одного слова латинскими буквами"""


config = Config()
