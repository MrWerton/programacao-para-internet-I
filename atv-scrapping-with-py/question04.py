import requests


def downloadImageFromUrl(url: str, name: str):
    response = requests.get(url)
    filename = name + ".png"
    with open(filename, "wb") as f:
        f.write(response.content)
