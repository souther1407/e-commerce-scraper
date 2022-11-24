from colorama import Fore
import random
import re
from constants import HTML_RESULT


class OutPut:

    def showScraping(self):
        print(Fore.BLUE, "Espere....")
        print(Fore.RESET)

    def showResults(self, results):
        pass


class FileOutPut(OutPut):
    def __init__(self) -> None:
        super().__init__()
        self.fileName = "resultados.html"

    def showResults(self, results):
        file = open(self.fileName, "w")
        rows = ""
        for result in results:
            rows += f"""<tr class="row">
                <td>{result['titulo']}</td>
                <td>${result['precio']}</td>
                <td>{result['link']}</td>
           </tr>\n"""

        html = f"""
                <tr class="header">
                    <th>Titulo</th>
                    <th>Precio</th>
                    <th>Link</th>
                 </tr>
                 {rows}
        """
       # data = re.sub(r"(<table>)+[\w\s<>=\"\/$./:\W]+(<\/table>)", html, data)
        file.write(HTML_RESULT.replace("contenido", html))
        file.close()
        print(Fore.BLUE, "Listo :D")


class ConsoleInterface(OutPut):
    def __init__(self) -> None:
        super().__init__()
        self.colors = [Fore.BLUE, Fore.CYAN,
                       Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    def getRandomColor(self):
        return self.colors[random.randint(0, len(self.colors)-1)]

    def cleanConsole():
        pass

    def showResults(self, result):
        print(
            f"------------------------- PRODUCTOS ({len(result)} resultados) ----------------------\r\n")
        if len(result) == 0:
            print("no se encontró ningun producto :C")
        for producto in result:
            print(
                f"titulo: {producto['titulo']}\r\nprecio: {producto['precio']}\r\nlink: {producto['link']}")
            print("////////////////////////////////////////////////////////\r\n")
