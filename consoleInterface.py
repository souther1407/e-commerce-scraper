class ConsoleInterface:
    def showResults(self, result):
        print(
            f"------------------------- PRODUCTOS ({len(result)} resultados) ----------------------\r\n")
        if len(result) == 0:
            print("no se encontró ningun producto :C")
        for producto in result:
            print(
                f"titulo: {producto['titulo']}\r\nprecio: {producto['precio']}\r\nlink: {producto['link']}")
            print("////////////////////////////////////////////////////////\r\n")
