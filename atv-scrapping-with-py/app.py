from urlValidator import UrlValidator
from question01 import getHrefs
from question02 import getContentInsideOfATag
from question03 import getTwentyBeforeAndAfterChar
import click


@click.group()
def main():
    pass


@main.command()
@click.option("--url", prompt="## insert a url: ", type=str)
def getUrls(url):
    if (UrlValidator(url)):
        result = getHrefs(url=url)
        for content in result:
            click.echo("link: {}".format(content))
    else:
        click.echo("url {} inserted not is valid".format(url))


@main.command()
@click.option("--url", prompt=" insert a url", type=str)
@click.option("--tag", prompt=" insert a tag", type=str)
def getContentInsideTag(url, tag):
    if (UrlValidator(url)):
        result = getContentInsideOfATag(url=url, tag=tag)
        for content in result:
            click.echo(
                "tag - {tag} && content - {content}".format(tag=tag, content=content))
    else:
        click.echo("url {} inserted not is valid".format(url))


@main.command()
@click.option("--url", prompt=" insert a url", type=str)
@click.option("--word", prompt=" insert a word", type=str)
def getTwentyBeforeAndAfterOfChar(url, word):
    if (UrlValidator(url)):
        result = getTwentyBeforeAndAfterChar(url=url, word=word)
        if (result):
            before = result[0]
            after = result[1]
            click.echo(
                "before - {before} && after - {after}".format(before=before, after=after))
        else:
            click.echo("not found {} in text".format(word))

    else:
        click.echo("url {} inserted not is valid".format(url))


if __name__ == "__main__":
    main()
