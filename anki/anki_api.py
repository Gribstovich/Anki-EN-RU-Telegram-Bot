from typing import Dict, Optional, Union, NoReturn

from base import invoke


def create_deck(deck_name: str) -> Dict[str, Optional[Union[int, None]]]:
    """
    Creates a new deck in Anki with the given name.

    :param deck_name: The name of the deck to be created.
    :return: A dictionary containing the result and any error.
        - 'result': The ID of the created deck (int) or None if an error occurred.
        - 'error': None if successful, otherwise an error message.
    """
    return invoke('createDeck', deck=deck_name)


def get_decks() -> Dict[str, Optional[Union[Dict[str, int], None]]]:
    """
    Retrieves all deck names and their corresponding IDs.

    :return: A dictionary containing deck names as keys and their IDs as values,
        or None if an error occurred.
        - 'result': A dictionary with deck names as keys and deck IDs as values.
        - 'error': None if successful, otherwise an error message.
    """
    return invoke('deckNamesAndIds')


def add_note(deck_name: str, front: str, back: str) -> Dict[str, Optional[Union[int, None]]]:
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
    return invoke('addNote', note=note)


def sync() -> NoReturn:
    """
    Synchronizes the local Anki collection with the AnkiWeb server.

    This function does not return any value. The response from Anki-Connect will always be:
    {"result": null, "error": null}
    """
    invoke('sync')
