from getHtml import HTMLdownloader
from htmlParser import HTMLParser


class MarketSource:
    def __init__(self, name, searchURL, resultHTLMComponent) -> None:
        self.name = name
        self.searchURL = searchURL
        self.resultHTLMComponent = resultHTLMComponent
        self.downloader = HTMLdownloader("file.html")

    def searchProducts(self, product):
        pass

    def getLinks(self, results):
        pass

    def getTitles(self, results):
        pass

    def getPrices(self, results):
        pass

    def createResult(self, titles, prices, links):
        results = []
        for i in range(len(titles)):
            results.append({
                "titulo": titles[i],
                "precio": prices[i],
                "link": links[i]
            })
        return results

    def parseProductName(self, product: str):
        return product.replace(" ", "%20")


class CompraGamerMarketSource(MarketSource):
    def __init__(self, name, searchURL, resultHTLMComponent) -> None:
        super().__init__(name, searchURL, resultHTLMComponent)
        self.site = "https://compragamer.com"

    def getLinks(self, results):
        links = []
        for result in results:
            links.append(self.site+result.div.contents[0].a.get("href"))
        return links

    def getPrices(self, results):
        prices = []
        for result in results:
            prices.append(result.div.find(
                "div", {"class": "contenedor-price"}).h1.span.get_text())
        return prices

    def getTitles(self, results):
        titles = []
        for result in results:
            titles.append(result.div.find(
                "div", {"class": "contenidoPrincipal"}).contents[0].find("span").get_text())
        return titles

    def searchProducts(self, product):
        total = []

        self.downloader.download(
            self.searchURL + "?seccion=3&criterio=" + self.parseProductName(product))

        f = open(self.downloader.getFilePath(), "r", encoding="utf8")
        data = f.read()
        f.close()

        parser = HTMLParser(data)

        resultsCards = parser.parseResults(
            self.resultHTLMComponent)

        if len(resultsCards) != 0:
            links = self.getLinks(resultsCards)
            titles = self.getTitles(resultsCards)
            prices = self.getPrices(resultsCards)
            total += self.createResult(titles, prices, links)

        return total


class AllMarketSource(MarketSource):

    def __init__(self, name, searchURL, resultHTLMComponent, marketSources) -> None:
        super().__init__(name, searchURL, resultHTLMComponent)
        self.marketSources = marketSources

    def getLinks(self, results):
        return super().getLinks(results)

    def getPrices(self, results):
        return super().getPrices(results)

    def getTitles(self, results):
        return super().getTitles(results)

    def searchProducts(self, product):
        results = []
        for marketSource in self.marketSources:
            results += marketSource.searchProducts(product)
        return results


class FullHardMarketSource(MarketSource):
    def __init__(self, name, searchURL, resultHTLMComponent) -> None:
        super().__init__(name, searchURL, resultHTLMComponent)
        self.site = "https://www.fullh4rd.com.ar"

    def getLinks(self, results):
        links = []
        for result in results:
            links.append(self.site+result.a.get("href"))
        return links

    def __parsePrice(self, rawPrice: str):
        firstPrice = rawPrice.split(" ")[0]
        return firstPrice[1:-3].replace(".", "")

    def getPrices(self, results):
        prices = []
        for result in results:
            price = result.find("div", {"class": "price"}).get_text()
            prices.append(self.__parsePrice(price))
        return prices

    def getTitles(self, results):
        titles = []
        for result in results:
            titles.append(result.find("div", {"class": "info"}).h3.get_text())
        return titles

    def searchProducts(self, product):
        total = []

        self.downloader.download(
            self.searchURL + self.parseProductName(product))

        f = open(self.downloader.getFilePath(), "r", encoding="utf8")
        data = f.read()
        f.close()

        parser = HTMLParser(data)

        resultsCards = parser.parseResults(
            self.resultHTLMComponent)

        if len(resultsCards) != 0:
            links = self.getLinks(resultsCards)
            titles = self.getTitles(resultsCards)
            prices = self.getPrices(resultsCards)
            total += self.createResult(titles, prices, links)

        return total


class MercadoLibreMarketSource(MarketSource):
    def __init__(self, name, searchURL, resultHTLMComponent) -> None:
        super().__init__(name, searchURL, resultHTLMComponent)

    def getLinks(self, results):
        links = []
        for result in results:
            links.append(result.div.div.a.get("href"))
        return links

    def getTitles(self, results):
        titles = []
        for result in results:
            titles.append(result.div.div.a.get("title"))
        return titles

    def getPrices(self, results):
        prices = []
        for result in results:
            prices.append(result.div.div.find(
                "span", {"class": "price-tag ui-search-price__part shops__price-part"}).span.get_text().split(" ")[0])
        return prices

    def searchProducts(self, product):
        cont = 0
        total = []

        while True:
            self.downloader.download(
                self.searchURL +
                self.parseProductName(
                    product)+f"_Desde_{cont*49-cont}_NoIndex_True"
            )
            f = open(self.downloader.getFilePath(), "r", encoding="utf8")
            data = f.read()
            f.close()
            parser = HTMLParser(data)

            resultsCards = parser.parseResults(
                self.resultHTLMComponent)

            if len(resultsCards) == 0:
                break

            links = self.getLinks(resultsCards)
            titles = self.getTitles(resultsCards)
            prices = self.getPrices(resultsCards)

            total += self.createResult(titles, prices, links)
            cont += 1
        return total
