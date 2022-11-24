from getHtml import HTMLdownloader
from marketSources import *
from consoleInterface import *
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
            HTMLComponent("div", {"class": "item product-list"})),

            "todo": AllMarketSource("todo", "", "", [
                MercadoLibreMarketSource(
                    "mercadolibre",
                    "https://listado.mercadolibre.com.ar/",
                    HTMLComponent(
                        "li", {"class": "ui-search-layout__item"}),
                ),
                FullHardMarketSource(
                    "fullhard",
                    "https://www.fullh4rd.com.ar/cat/search/",
                    HTMLComponent("div", {"class": "item product-list"}))
            ]),
            "compragamer": CompraGamerMarketSource(
                "compragamer",
                "https://compragamer.com/",
                HTMLComponent("cgw-product-alone", {"class": "mat-card card-product ng-star-inserted"}))

        }
        self.interfaces = {"si": FileOutPut(), "no": ConsoleInterface()}

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

        filtered = []
        for product in results:
            if int(product["precio"]) >= orders.minimo and int(product["precio"]) < orders.maximo:
                filtered.append(product)

        if orders.limite > 0:
            filtered = filtered[0:orders.limite]

        return filtered

    def getResults(self, product, orders):
        self.interfaces[orders.archivo].showScraping()
        result = self.marketSources[orders.mercado].searchProducts(product)

        result = self.__executeOrders(result, orders)
        self.interfaces[orders.archivo].showResults(result)
