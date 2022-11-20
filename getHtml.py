import requests


class HTMLdownloader:
    def __init__(self, filePath=""):

        self.__filePath = filePath

    def download(self, url):
        try:
            response = requests.get(url)
            file = open(self.__filePath, "w", encoding="utf-8")
            file.write(response.text)
            file.close()
        except requests.exceptions.ConnectionError as err:
            print(err)
        except Exception as err:
            print(err)

    def setFilePath(self, filePath):
        self.__filePath = filePath

    def getFilePath(self):
        return self.__filePath
