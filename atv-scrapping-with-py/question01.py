import requests
from regexDecorator import RegexDecorator


def getHrefs(url: str):
    response = requests.get(url)
    result = RegexDecorator.getHrefs(document=response.text)
    return result
