import requests
from regex import Regex


def getContentInsideOfATag(url: str, tag: str):
    response = requests.get(url)
    result = Regex.getContentInsideOfTag(
        document=response.text, tag=tag)
    return result
