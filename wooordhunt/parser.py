from dataclasses import dataclass
from typing import Optional, List, Tuple, Union

import requests

MAIN_URL = 'https://wooordhunt.ru'


@dataclass
class WordDetails:
    name: str
    rank: Optional[int]
    transcription: Optional[str]
    description: Optional[str]
    examples: Union[List[Tuple[str, str]], None]


def fetch_page(url: str) -> Optional[str]:
    """
    Fetch the content of a page from a given URL.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        Optional[str]: The HTML content of the page, or None if an error occurred.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f'Error fetching page: {e}')
        return None
