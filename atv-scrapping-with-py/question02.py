import requests
from regexDecorator import RegexDecorator


def getContentInsideOfATag(url: str, tag: str):
    response = requests.get(url)
    result = RegexDecorator.getContentInsideOfTag(
        document=response.text, tag=tag)
    return result
