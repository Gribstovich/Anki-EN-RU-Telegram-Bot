from dataclasses import dataclass
from typing import Optional, List, Tuple, Union

import requests
from bs4 import BeautifulSoup

MAIN_URL = 'https://wooordhunt.ru'


@dataclass
class WordDetails:
    name: str
    rank: Optional[int]
    transcription: Optional[str]
    description: Optional[str]
    examples: Union[List[Tuple[str, str]], None]


def parse_word(page_content: str) -> WordDetails:
    """
    Parse the HTML content of the page to extract word details.

    Args:
        page_content (str): The HTML content of the page.

    Returns:
        WordDetails: An instance of WordDetails with parsed word details.
    """
    soup = BeautifulSoup(page_content, 'lxml')
    return WordDetails(
        name=get_word_name(soup),
        rank=get_word_rank(soup),
        transcription=get_word_transcription(soup),
        description=get_word_description(soup),
        examples=get_word_examples(soup)
    )


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


def get_word(word: str) -> Optional[WordDetails]:
    """
    Retrieve detailed description of a word from the website.

    Args:
        word (str): The word to retrieve information for.

    Returns:
        Optional[WordDetails]: An instance of WordDetails with details about the word, or None if the word is not found.
    """
    url = f'{MAIN_URL}/word/{word}'
    page_content = fetch_page(url)
    return parse_word(page_content) if page_content else None


def get_word_name(soup: BeautifulSoup) -> str:
    """
    Extract the word name from the page content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the page content.

    Returns:
        str: The word name, or a default message if not found.
    """
    word_name = soup.find(['h1', 'h2'])
    return word_name.text.strip().capitalize() if word_name else None


def get_word_rank(soup: BeautifulSoup) -> Optional[int]:
    """
    Extract the rank of the word from the page content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the page content.

    Returns:
        Optional[int]: The word rank, or None if not found or invalid.
    """
    rank_element = soup.find(id='word_rank_box')
    try:
        return int(rank_element.text.strip()) if rank_element else None
    except ValueError:
        return None


def get_word_transcription(soup: BeautifulSoup) -> Optional[str]:
    """
    Extract the transcription of the word from the page content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the page content.

    Returns:
        Optional[str]: The word transcription, or None if not found.
    """
    uk_tr_sound = soup.find(id='uk_tr_sound')
    if uk_tr_sound:
        transcription = uk_tr_sound.text.strip().split()[-1]
        return f'[{transcription[1:-1]}]'
    return None


def get_word_description(soup: BeautifulSoup) -> Optional[str]:
    """
    Extract a short description of the word from the page content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the page content.

    Returns:
        Optional[str]: The short description of the word, or None if not found.
    """
    description = soup.find('div', class_='t_inline_en')
    return description.text.strip().capitalize() if description else None


def get_word_examples(soup: BeautifulSoup) -> Union[List[Tuple[str, str]], str]:
    """
    Extract usage examples of the word from the page content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the page content.

    Returns:
        Union[List[Tuple[str, str]], str]: A list of tuples where each tuple contains an original example and its translation, or a default message if not found.
    """
    original_texts = soup.find_all('p', class_='ex_o')
    translated_texts = soup.find_all('p', class_='ex_t')

    examples = [(orig.get_text(strip=True), trans.get_text(strip=True))
                for orig, trans in zip(original_texts, translated_texts)]

    return examples if examples else None
