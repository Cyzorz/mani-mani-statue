from os import path

class Path:
    @staticmethod
    def get(file):
        return path.join(path.dirname(path.dirname(path.abspath(__file__))), file)