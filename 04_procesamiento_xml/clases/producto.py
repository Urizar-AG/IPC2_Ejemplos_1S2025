class Producto:
    def __init__(self, nombre, pasillo, estante, stock):
        self.__nombre = nombre
        self.__pasillo = pasillo
        self.__estante = estante
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre
    
    def get_pasillo(self):
        return self.__pasillo
    
    def get_estante(self):
        return self.__estante
    
    def get_stock(self):
        return self.__stock

    def get_detalles(self):
        print(f'Producto: {self.__nombre}\nUbicación: Pasillo {self.__pasillo} - Estante: {self.__estante}\nStock:{self.__stock}')

