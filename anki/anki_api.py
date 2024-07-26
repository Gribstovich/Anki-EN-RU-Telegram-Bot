from typing import Dict, Optional, Union, NoReturn

from anki.base import invoke


async def get_decks() -> list[str]:
    """
    Retrieves all deck names that do not have children decks.

    :return: A list of deck names without children.
    """
    all_decks = await invoke('deckNames')
    decks_without_children = [
        deck for deck in all_decks
        if deck != 'По умолчанию' and not any(inner_deck.startswith(f'{deck}::') for inner_deck in all_decks)
    ]
    return sorted(decks_without_children)


async def add_note(deck_name: str, front: str, back: str) -> Dict[str, Optional[Union[int, None]]]:
    """
    Adds a new note to the specified deck.

    :param deck_name: The name of the deck to which the note will be added.
    :param front: The text for the front field of the note.
    :param back: The text for the back field of the note.
    :return: A dictionary containing the result and any error.
        - 'result': The ID of the added note (int) or None if an error occurred.
        - 'error': None if successful, otherwise an error message.
    """
    note = {
        'deckName': deck_name,
        'modelName': 'Basic',
        'fields': {
            'Front': front,
            'Back': back,
        },
        'options': {
            'allowDuplicate': False,
            'duplicateScope': 'deck'
        }
    }
    return await invoke('addNote', note=note)


async def sync() -> NoReturn:
    """
    Synchronizes the local Anki collection with the AnkiWeb server.

    This function does not return any value. The response from Anki-Connect will always be:
    {"result": null, "error": null}
    """
    await invoke('sync')
