import requests
from regexDecorator import RegexDecorator


def getTwentyBeforeAndAfterChar(url: str, word: str):
    response = requests.get(url)
    result = RegexDecorator.getTwentyBeforeAndAfterChar(
        document=response.text, word=word)
    return result


re = getTwentyBeforeAndAfterChar(
    url="https://www.comunicareapraxia.com/", word="aaaa")

print(re)
