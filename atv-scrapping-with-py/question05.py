import requests


def searchInGoogle(term: str):

    result = requests.get(
        "https://www.google.com/search?q={term}".format(term=term))

    return result.text
