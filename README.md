# WooordHunt to Anki Bot
![Works with Python versions 3.8-3.12](https://img.shields.io/badge/Python-%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20-0B61A4)
![Aiogram 3.10](https://img.shields.io/badge/Aiogram-3.10-FFAA00)
![GPL-3.0 license](https://img.shields.io/github/license/Gribstovich/WooordHunt-to-Anki-Bot?color=FF7400)

## About the Project
A Telegram bot that generates English word cards using WooordHunt and adds them to your Anki collection.

**Note:** This bot is not for general use, each user should run it on their own private server. The reason is that it does not store cards and decks in a database, it uses your personal Anki profile.

### How It Works
1. You send the bot a word in English.
2. The bot requests the [WooordHunt](https://wooordhunt.ru) service, parses the response, and returns the word's information.
3. Optionally, the bot generates an [Anki](https://ankiweb.net/about) card and adds it to your deck.

## Prerequisites
- Anki application (version 2.1 or later) with the Anki-Connect plugin installed.
- Python 3.8 to 3.12.
- A Telegram bot token from BotFather.

### Installation of Anki and Anki-Connect
- [How to install Anki](https://docs.ankiweb.net/getting-started.html#installing--upgrading)
- [How to install Anki-Connect](https://foosoft.net/projects/anki-connect)

### Creating a Telegram Bot
- [How to create a bot](https://core.telegram.org/bots/features#creating-a-new-bot)

## Installation and Startup
### For Debian-based Distros
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Gribstovich/WooordHunt-to-Anki-Bot.git
    cd WooordHunt-to-Anki-Bot
    ```
2. **Create and Activate a Virtual Environment:**
    ```bash
    sudo apt install python3 python3-pip
    python3 -m venv env
    source env/bin/activate
    ```
3. **Install Dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```
4. **Configure the .env File:**
    - Rename the file `telegram/.env.example` to `telegram/.env` and edit it as instructed in the comments.
5. **Start the Bot:**
    ```bash
    python3 telegram/bot.py
    ```

## License
This project is licensed under the GPL-3.0 License. For more details, see the [LICENSE.md](LICENSE.md) file.

## Acknowledgments
Hat tip to the contributors of [aiogram](https://github.com/aiogram/aiogram) and [Anki](https://github.com/ankitects/anki), and to FooSoft for [Anki-Connect](https://github.com/FooSoft/anki-connect).
