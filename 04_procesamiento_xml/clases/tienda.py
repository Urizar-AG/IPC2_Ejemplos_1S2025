class Tienda:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.productos = None

    def get_nombre(self):
        return self.__nombre
