import requests


def getAddessByCep(cep: str):

    result = requests.get(
        "https://viacep.com.br/ws/{cep}/json/".format(cep=cep))
    data = result.text

    return data
