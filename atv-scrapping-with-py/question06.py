import requests
from regex import Regex


def getTable(url: str):
    response = requests.get(url)

    result = Regex.getTable(
        document=response.text)
    return result
