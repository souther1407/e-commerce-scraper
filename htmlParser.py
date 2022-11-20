from bs4 import BeautifulSoup


class HTMLParser:
    def __init__(self, data) -> None:
        self.soup = BeautifulSoup(data, "html.parser")

    def parseResults(self, resultHTLMComponent):

        return self.soup(resultHTLMComponent.type, resultHTLMComponent.attributes)
