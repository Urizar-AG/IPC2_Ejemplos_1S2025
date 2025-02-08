from clases.persona import Persona #Importando la clase Persona

class Estudiante(Persona): #Estudiante extiende de Persona
    def __init__(self, nombre, edad, carnet):
        super().__init__(nombre, edad) #Constructor de la superclase (clase Persona)
        self.__carnet = carnet
    
    def get_carnet(self):
        return self.__carnet

    def set_carnet(self, carnet):
        self.__carnet = carnet

    def saludar(self):
        print(f'Hola soy {self.get_nombre()}, tengo {self.get_edad()} años')
        print(f'Mi carnet es {self.__carnet}')