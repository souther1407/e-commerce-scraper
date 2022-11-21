from getHtml import HTMLdownloader
from marketSources import *
from consoleInterface import ConsoleInterface
from constants import *


class HTMLComponent:
    def __init__(self, type, attr) -> None:
        self.type = type
        self.attributes = attr


class Scrapper:
    def __init__(self) -> None:
        self.marketSources = {"mercadolibre": MercadoLibreMarketSource(
            "mercadolibre",
            "https://listado.mercadolibre.com.ar/",
            HTMLComponent("li", {"class": "ui-search-layout__item"}),
        ),
            "fullhard": FullHardMarketSource(
            "fullhard",
            "https://www.fullh4rd.com.ar/cat/search/",
            HTMLComponent("div", {"class": "item product-list"}))
        }

        self.interface = ConsoleInterface()

    def sortByPrice(self, result):
        return int(result['precio'].split(' ')[0])

    def sortByTitle(self, result):
        return result["titulo"]

    def __executeOrders(self, results: list, orders):
        if len(results) == 0:
            return results

        if orders.ordenar == SORT_PRICE_ASC:
            results.sort(key=self.sortByPrice)
        elif orders.ordenar == SORT_PRICE_DESC:
            results.sort(key=self.sortByPrice, reverse=True)
        elif orders.ordenar == SORT_TITLE_ASC:
            results.sort(key=self.sortByTitle)
        elif orders.ordenar == SORT_TITLE_DESC:
            results.sort(key=self.sortByTitle, reverse=True)

        if orders.limite > 0:
            results = [results[i] for i in range(
                orders.limite if orders.limite <= len(results) else len(results))]

        filtered = []
        for product in results:
            if int(product["precio"]) >= orders.minimo and int(product["precio"]) < orders.maximo:
                filtered.append(product)

        return filtered

    def getResults(self, product, orders):
        result = self.marketSources[orders.mercado].searchProducts(product)

        result = self.__executeOrders(result, orders)

        self.interface.showResults(result)
