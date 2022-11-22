from colorama import Fore
import random


class ConsoleInterface:
    def __init__(self) -> None:
        self.colors = [Fore.BLUE, Fore.CYAN,
                       Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    def getRandomColor(self):
        return self.colors[random.randint(0, len(self.colors)-1)]

    def cleanConsole():
        pass

    def showScraping(self):
        print(Fore.BLUE, "Espere....")
        print(Fore.RESET)

    def showResults(self, result):
        print(
            f"------------------------- PRODUCTOS ({len(result)} resultados) ----------------------\r\n")
        if len(result) == 0:
            print("no se encontró ningun producto :C")
        for producto in result:
            print(
                f"titulo: {producto['titulo']}\r\nprecio: {producto['precio']}\r\nlink: {producto['link']}")
            print("////////////////////////////////////////////////////////\r\n")
