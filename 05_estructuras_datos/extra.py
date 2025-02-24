from lista_doble.lista_doble import ListaDoble

class Nodo:
    def __init__(self, carnet):
        #Dato
        self.__carnet = carnet
        self.__libros = ListaDoble() #Cada nodo de la lista simple tendrá su propia lista doble
        #Apuntador al siguiente nodo
        self.siguiente = None

    def get_carnet(self):
        return self.__carnet
    
    def get_libros(self):
        return self.__libros
    
class ListaSimple:
    def __init__(self):
        self.primero = None #Referencia al primer nodo de  la lista (head)

    #Insertar nodo al final de la lista
    def insertar_final(self, carnet):
        nuevo = Nodo(carnet) 
        if self.primero is None:
            self.primero = nuevo
        else: #Hay por lo menos un nodo en la lista
            tmp = self.primero 
            while tmp.siguiente is not None:
                tmp = tmp.siguiente 
            tmp.siguiente = nuevo

    #Obtiene un nodo de la lista
    def buscar(self, carnet):
        tmp = self.primero #Nodo auxiliar para recorrer la lista
        while tmp:
            if tmp.get_carnet() == carnet:
                return tmp
            tmp = tmp.siguiente
        return None #No encontro el carnet retorna nulo
    
    #Imprimir todos los nodos de la lista
    def mostrar_lista(self):
        print('Listado estudiantes')
        print('================================')

        tmp = self.primero
        while tmp: #Recorre la lista mientras temporal no sea Nulo (None)
            print('Carnet: ', tmp.get_carnet())

            #Accede a los métodos de la lista doble
            print('Libros:')
            tmp.get_libros().mostrar_lista() 

            tmp = tmp.siguiente
            print('================================')

if __name__ == '__main__':
    listado = ListaSimple()
    listado.insertar_final(1)
    listado.insertar_final(2)

    estudiante = listado.buscar(1)
    #Accede a los métodos de la lista doble
    estudiante.get_libros().insertar_final(1234, 'Frankenstein', 'Mary Shelley')
    estudiante.get_libros().insertar_final(5678, 'La Metamorfosis', 'Franz Kafka')
    # estudiante.get_libros().mostrar_lista() #Este es el método mostrar_lista de la lista doble

    estudiante2 = listado.buscar(2)
    estudiante2.get_libros().insertar_final(9012, 'El Principito', 'Antoine de Saint-Exupery')

    listado.mostrar_lista()
