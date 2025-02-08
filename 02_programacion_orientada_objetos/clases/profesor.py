from clases.persona import Persona #Importando la clase Persona

class Profesor(Persona): #Profesor extiende de Persona
    def __init__(self, nombre, edad, id, salario):
        super().__init__(nombre, edad) #Constructor de la superclase (clase Persona)
        self.__id = id
        self.__salario = salario
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def saludar(self):
        print(f'Hola soy el profesor {self.get_nombre()}, tengo {self.get_edad()} años')

    def describir(self):
        print(f'Mi ID es {self.__id} y mi salario es de {self.__salario}')
