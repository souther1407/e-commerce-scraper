import re


f = open("resultados.html", "r+")

data = f.read()
print(re.sub(r"(<table>)+[\w\s<>=\"\/$./:]+(<\/table>)", "holaa", data))
