import graphviz

class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None

    def get_data(self):
        return self.__data

class Stack:
    def __init__(self):
        self.__top = None #Apuntador a la cima o primer nodo de la pila
        self.__size = 0

    #Agregrar un nodo al final de la pila
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.__top
        self.__top = new_node
        self.__size += 1 #Actualizar el tamaño de la lista

    #Eliminar el primer nodo de la pila
    def pop(self):
        if self.__top is None:
            print('No hay elementos en la pila')
        else:
            value = self.__top.get_data() #Obtener el valor del nodo a eliminar

            temporal = self.__top
            self.__top = temporal.next
            temporal.next = None
    
            #Actualizar el tamaño de la lista
            self.__size -= 1 

            return value #Devuelve el valor eliminado
        
    #Obtener el primer nodo de la pila
    def peek(self):
        return self.__top

    #Verificar si la cola Pila vacía
    def is_empty(self):
        return self.__top is None
    
    #Obtener el tamaño de la Pila
    def stack_size(self):
        return self.__size

    #Recorrer la pila
    def print_stack(self):
        temporal = self.__top
        while temporal:
            print(temporal.get_data())
            temporal = temporal.next
    
    #Graficar la pila
    def draw_stack(self, path):
        dot = graphviz.Digraph(format='svg', name='Cola')
        dot.attr(label='Pila', labelloc='t')
        dot.attr(rankdir='TB') #Dirección de la gráfica -> Left to Right
        dot.attr('node', shape='record')
        dot.attr('edge', arrowtail='dot', dir='both')

        aux = 1
        temporal = self.__top
        while temporal:
            dot.node(str(aux), f'{{{temporal.get_data()}|}}')
            if temporal != self.__top:
                #Enlazar los nodos
                dot.edge(str(aux - 1), str(aux))
            temporal = temporal.next
            aux += 1
        dot.render(path, view=True)
