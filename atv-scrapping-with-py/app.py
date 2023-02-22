from urlValidator import UrlValidator
from question01 import getHrefs
from question02 import getContentInsideOfATag
from question03 import getTwentyBeforeAndAfterChar
from question04 import downloadImageFromUrl
from question05 import searchInGoogle
import click


while True:
    question = input(
        """
          1 - get all the links from web page
          2 - get content inside tag
          3 - get the 20 before and after char in of a determinate word
          4 - download image from url
          5 - search term in google

          0 - exit
        """)
    if question == '0':
        break
    elif question == '1':
        url = input("insert a url: ")

        if (UrlValidator(url)):
            result = getHrefs(url=url)
            for content in result:
                print("link: {}".format(content))
        else:
            print("url {} inserted not is valid".format(url))
    elif question == '2':
        url = input("insert a url: ")
        if (UrlValidator(url)):
            tag = input("insert a tag: ")
            result = getContentInsideOfATag(url=url, tag=tag)
            for content in result:
                print(
                    "tag - {tag} && content - {content}".format(tag=tag, content=content))
        else:
            print("url {} inserted not is valid".format(url))
    elif question == '3':
        url = input("insert a url: ")
        if (UrlValidator(url)):
            word = input(
                "insert a word for search the after and before char: ")
            result = getTwentyBeforeAndAfterChar(url=url, word=word)
            if (result):
                before = result[0]
                after = result[1]
                click.echo(
                    "before - {before} && after - {after}".format(before=before, after=after))
            else:
                print("not found {} in text".format(word))
        else:
            print("url {} inserted not is valid".format(url))
    elif question == '4':
        url = input("insert a url: ")
        if (UrlValidator(url)):
            name = input(
                "insert a name of image: ")
            downloadImageFromUrl(url=url, name=name)
            print("image was downloaded with success")
        else:
            print("url {} inserted not is valid".format(url))
    elif question == '5':
        name = input(
            "insert a term of search in google: ")
        result = searchInGoogle(term=name)
        print(result)

    else:
        print(f"Command not found")
