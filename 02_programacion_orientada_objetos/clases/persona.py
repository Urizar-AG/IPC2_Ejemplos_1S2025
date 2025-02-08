class Persona:
    def __init__(self, nombre, edad): #Método constructor
        self.__nombre = nombre #Si eliminamos los guiones bajos el atributo se vuelve público
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

    def saludar(self):
        pass

if __name__ == "__main__":
    persona = Persona("Pablo", 20)
    print(persona.get_nombre())
    print(persona.get_edad())
   
    print("--------------------------")

    persona.set_nombre('Juan')
    print(persona.get_nombre())
    print(persona.get_edad())
