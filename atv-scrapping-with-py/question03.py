import requests
from regex import Regex


def getTwentyBeforeAndAfterChar(url: str, word: str):
    response = requests.get(url)
    result = Regex.getTwentyBeforeAndAfterChar(
        document=response.text, word=word)
    return result


re = getTwentyBeforeAndAfterChar(
    url="https://www.comunicareapraxia.com/", word="aaaa")

print(re)
