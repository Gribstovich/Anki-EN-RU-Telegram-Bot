from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from anki import anki_api


async def generate_deck_keyboard() -> InlineKeyboardMarkup:
    """
    Generates an inline keyboard for selecting Anki decks.

    The keyboard will display buttons for each deck, arranged in rows of three buttons.
    The last row will always contain button 'Don't Save'.

    :return: An instance of InlineKeyboardMarkup containing the generated keyboard.
    """
    builder = InlineKeyboardBuilder()
    decks = await anki_api.get_decks()

    deck_buttons = [
        InlineKeyboardButton(text=deck.split(':')[-1], callback_data=deck) for deck in decks
    ]

    num_buttons = len(deck_buttons)
    if num_buttons:
        buttons_per_row = 3
        for i in range(0, num_buttons, buttons_per_row):
            builder.row(*deck_buttons[i:i + buttons_per_row])

    builder.row(InlineKeyboardButton(text='❌ Не сохранять', callback_data="Don`t_Save"))

    return builder.as_markup()
