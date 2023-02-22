import re


class Regex:
    @staticmethod
    def getHrefs(document: str):
        regex = r'href=[\'"]?([^\'" >]+)'
        result = re.findall(regex, document)
        if result:
            return result
        else:
            message = 'not found hrefs'
            return [message]

    @staticmethod
    def getContentInsideOfTag(tag: str, document: str):
        regex = r'<{tag}.*?>(.*?)</{tag}>'.format(tag=tag)
        result = re.findall(regex, document)
        if result:
            return result
        else:
            message = 'not found result with the tag ' + tag
            return [message]

    @staticmethod
    def getTwentyBeforeAndAfterChar(document, word):
        sensitivePattern = re.compile(word, re.IGNORECASE)
        result = re.search(sensitivePattern, document)
        if result:
            before = document[(result.start() - 20):result.start()]
            after = document[result.end():result.end() + 20]
            return [before, after]
        else:
            return None
