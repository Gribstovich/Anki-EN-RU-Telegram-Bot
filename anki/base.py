import json
from typing import Any, Dict, Union

import requests


def request(action: str, **params: Any) -> Dict[str, Union[str, Dict[str, Any]]]:
    """
    Forms a JSON request for the specified action and parameters.

    :param action: The action to be performed.
    :param params: Additional parameters for the action.
    :return: A dictionary representing the request.
    """
    return {'action': action, 'params': params, 'version': 6}


def invoke(action: str, **params: Any) -> Any:
    """
    Sends a request to the local server running the Anki application with the Anki-Connect extension
    and processes the response. The Anki-Connect extension must be installed in the Anki application.


    :param action: The action to be performed.
    :param params: Additional parameters for the action.
    :return: The result of the action.
    :raises Exception: If the HTTP request fails or the response contains an error.
    """
    try:
        request_json = json.dumps(request(action, **params))
        response = requests.post(url='http://127.0.0.1:8765',
                                 data=request_json,
                                 headers={'Content-Type': 'application/json'})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f'HTTP request failed: {e}')

    try:
        response_json = response.json()
    except json.JSONDecodeError as e:
        raise Exception(f'Failed to decode JSON response: {e}')

    if 'error' not in response_json or 'result' not in response_json:
        raise Exception('Response is missing required fields')
    if response_json['error'] is not None:
        raise Exception(response_json['error'])

    return response_json['result']
