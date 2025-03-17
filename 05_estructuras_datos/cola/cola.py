import graphviz

class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None

    def get_data(self):
        return self.__data

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    #Agregar un elemento en la cola, se agrega el nodo siempre al final de la lista
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.__head is None: 
            #Si la cola está vacía
            self.__head = self.__tail = new_node
        else:
            #Hay al menos un nodo en la cola
            self.__tail.next = new_node
            self.__tail = new_node
        
        #Aumentar el tamaño de la lista
        self.__size += 1

    #Eliminar un elemento de la cola, se elimina siempre el primer nodo de la lista
    def dequeue(self):
        if self.__head is None:
            print('No hay elementos en la cola')
        else:
            temporal = self.__head
            self.__head = temporal.next
            temporal.next = None

            #Actualizar el tamaño de la lista
            self.__size -= 1 
            
    #Obtener el primer nodo de la cola
    def peek(self):
        return self.__head

    #Verificar si la cola está vacía
    def is_empty(self):
        return self.__head is None
    
    #Obtener el tamaño de la cola
    def queue_size(self):
        return self.__size
    
    #Recorrer la cola
    def print_queue(self):
        temporal = self.__head
        while temporal:
            print(temporal.get_data())
            temporal = temporal.next
    
    #Graficar la cola
    def draw_queue(self, path):
        dot = graphviz.Digraph(format='svg', name='Cola')
        dot.attr(label='Cola', labelloc='t')
        dot.attr(rankdir='LR') #Dirección de la gráfica -> Left to Right
        dot.attr('node', shape='record')
        dot.attr('edge', arrowtail='dot', dir='both')

        aux = 1
        temporal = self.__head
        while temporal:
            dot.node(str(aux), f'{{{temporal.get_data()}|}}')
            if temporal != self.__head:
                #Enlazar los nodos
                dot.edge(str(aux - 1), str(aux))
            temporal = temporal.next
            aux += 1
        dot.render(path, view=True)
        