import requests
from regex import Regex


def getHrefs(url: str):
    response = requests.get(url)
    result = Regex.getHrefs(document=response.text)
    return result
