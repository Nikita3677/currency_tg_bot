import requests
from http import HTTPStatus


def make_request(URL):
    response = requests.get(URL)
    if response.status_code == HTTPStatus.OK:
        return response