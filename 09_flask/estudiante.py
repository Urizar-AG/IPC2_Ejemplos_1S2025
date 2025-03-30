class Estudiante:
    def __init__(self, carnet, nombre, correo):
        self.__carnet = carnet
        self.__nombre = nombre
        self.__correo = correo
    
    def get_carnet(self):
        return self.__carnet
    
    def get_nombre(self):
        return self.__nombre
    
    def get_correo(self):
        return self.__correo
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_correo(self, correo):
        self.__correo = correo

    def get_info(self):
        return {
            'carnet': self.__carnet,
            'nombre': self.__nombre,
            'correo': self.__correo
        }