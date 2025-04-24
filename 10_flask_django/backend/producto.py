class Producto:
    def __init__(self, id, nombre, marca, precio, stock):
        self.__id = id
        self.__nombre = nombre
        self.__marca = marca
        self.__precio = precio
        self.__stock = stock

    def get_id(self):
        return self.__id
    
    def get_info(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'marca': self.__marca,
            'precio': self.__precio,
            'stock': self.__stock
        }
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_marca(self, marca):
        self.__marca = marca

    def set_precio(self, precio):
        self.__precio = precio

    def set_stock(self, stock):
        self.__stock = stock
