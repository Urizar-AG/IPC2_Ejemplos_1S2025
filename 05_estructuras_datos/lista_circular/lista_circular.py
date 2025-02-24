import os

class Nodo:
    def __init__(self, dato):
        #Dato
        self.__dato = dato

        #Apuntador al siguiente nodo
        self.siguiente = None

    def get_dato(self):
        return self.__dato
    
class ListaCircular:
    def __init__(self):
        self.primero = None

    #Insertar nodo al inicio de la lista
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None: #La lista está vacía
            self.primero = nuevo
            nuevo.siguiente = self.primero
        else: #Hay por lo menos un nodo en la lista
            nuevo.siguiente = self.primero
            tmp = self.primero 
            while tmp.siguiente != self.primero:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.primero = nuevo

    
    #Agregar un nuevo elemento al final de la lista
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None: #La lista está vacía
            self.primero = nuevo
            nuevo.siguiente = self.primero
        else: #Hay por lo menos un nodo en la lista
            tmp = self.primero #Nodo auxiliar para recorrer la lista
            while tmp.siguiente != self.primero:
                tmp = tmp.siguiente #tmp ahora es el nodo siguiente

            tmp.siguiente = nuevo
            nuevo.siguiente = self.primero #Apunta el último nodo al primer nodo
    
    #Buscar un nodo de la lista
    def buscar(self, dato):
        tmp = self.primero
        while tmp:
            if tmp.get_dato() == dato:
                return tmp
            tmp = tmp.siguiente

            #Ya recorrio toda la lista e iniciaria de nuevo
            if tmp == self.primero:
                break
        return None
    
    #Eliminar un nodo de la lista
    def eliminar(self, dato):
        if self.primero is None:
            print('La lista está vacía')
        elif self.primero.get_dato() == dato: #El nodo a eliminar es el primero en la lista
            tmp = self.primero
            self.primero = tmp.siguiente #Primero ahora apunta al segundo nodo
            tmp.siguiente = None
            print('Nodo eliminado correctamente')
        else:
            prev = self.primero #Nodo anterior al que se está borrando
            tmp = self.primero.siguiente #Nodo a borrar
            while tmp:
                if tmp.get_dato() == dato:
                    prev.siguiente = tmp.siguiente
                    tmp.siguiente = None
                    print('Nodo eliminado correctamente')
                    return
                prev = tmp 
                tmp = tmp.siguiente

            print('No fue posible eliminar, el carnet no existe')
    
    #Mostrar todos los nodos de la lista
    def mostrar_lista(self):
        tmp = self.primero
        while tmp: #Recorre la lista mientras temporal no sea Nulo (None)
            print(tmp.get_dato())
            tmp = tmp.siguiente
            if tmp == self.primero:
                break

    #Generar la gráfica de la lista
    def graficar_lista(self, archivo):
        with open(f'{archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\trankdir=LR;\n')  #Dibuja el grafo de izquierda a derecha
            file.write('\tlabel="Listado de estudiantes"\n') #Título de la gráfica
            file.write('\tlabelloc = t;\n') #Ubicación del título
            file.write('\tnode [shape = record];\n') #Definir características de los nodos, en este caso la forma
            
            # Recorre la lista para agregar los nodos y sus conexiones
            contador = 0
            tmp = self.primero
            while tmp:
                file.write(f'\tnode{contador} [label="{{Carnet: {tmp.get_dato()}}}"];\n')
                if tmp != self.primero:
                    file.write(f'\tnode{contador-1} -> node{contador};\n') #Enlaza el nodo anterior con el nodo actual
                tmp = tmp.siguiente
                if tmp == self.primero:
                    break
                contador += 1
            file.write(f'\tnode{contador} -> node{0} [constraint=false];\n') #Apuntador del primer nodo al último nodo
            file.write('}')
        os.system("dot -Tsvg "+ archivo +".dot -o "+ archivo +".svg")
