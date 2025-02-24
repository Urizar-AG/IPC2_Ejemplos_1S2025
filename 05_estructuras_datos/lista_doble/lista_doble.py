import os

class Nodo:
    def __init__(self, codigo, titulo, autor):
        #Dato
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor

        #Apuntadores
        self.siguiente = None #Apuntador al siguiente Nodo
        self.anterior = None  #Apuntador al nodo anterior

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def mostrar_info(self):
        print(f'Código: {self.__codigo} - Título: {self.__titulo} - Autor: {self.__autor}')

class ListaDoble:
    def __init__(self):
        self.primero = None #Referencia la primer nodo de la lista (head)
        self.ultimo = None #Apuntador al último nodo de la lista

    #Insertar nodo al inicio de la lista
    def insertar_inicio(self, codigo, titulo, autor):
        nuevo = Nodo(codigo, titulo, autor)
        if self.primero is None: #La lista está vacía
            self.primero = self.ultimo = nuevo
        else: #Hay por lo menos un nodo en la lista
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo #Mueve el apuntador al nuevo primer nodo

    #Insertar nodo al final de la lista
    def insertar_final(self, codigo, titulo, autor):
        nuevo = Nodo(codigo, titulo, autor)
        if self.primero is None: #La lista está vacía
            self.primero = self.ultimo = nuevo
        else: #Hay por lo menos un nodo en la lista
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo #Mueve el apuntador al nuevo último nodo

    #Obtiene un nodo de la lista
    def buscar(self, codigo): 
        tmp = self.primero #Inicia el recorrido al inicio de la lista
        while tmp:
            if tmp.get_codigo() == codigo:
                return tmp
            tmp = tmp.siguiente
        return None #No encontro el carnet, retorna nulo
    
    #Obtiene un nodo de la lista
    def buscar_reverso(self, codigo):
        tmp = self.ultimo #Inicia el recorrido al final de la lista
        while tmp:
            if tmp.get_codigo() == codigo:
                return tmp
            tmp = tmp.anterior
        return None
    
    #Eliminar nodo de la lista
    def eliminar(self, codigo):
        tmp = self.primero
        if self.primero is None:
            print('La lista está vacía')
            return
        
        tmp = self.primero
        while tmp:
            if tmp.get_codigo() == codigo:
                if tmp == self.primero:
                    self.primero = tmp.siguiente
                    tmp.siguiente = None
                    self.primero.anterior = None
                    print('Nodo eliminado correctamente')
                    return
                elif tmp == self.ultimo:
                    self.ultimo = tmp.anterior
                    tmp.anterior = None
                    self.ultimo.siguiente = None
                    print('Nodo eliminado correctamente')
                    return
                else:
                    tmp.anterior.siguiente = tmp.siguiente
                    tmp.siguiente.anterior = tmp.anterior
                    tmp.siguiente = None
                    tmp.anterior = None
                    print('Nodo eliminado correctamente')
                    return
            tmp = tmp.siguiente
        print('No fue posible eliminar, el codigo no existe')

    #Imprimir todos los nodos de la lista
    def mostrar_lista(self):
        tmp = self.primero
        while tmp: #Recorre la lista mientras temporal no sea Nulo (None)
            tmp.mostrar_info()
            tmp = tmp.siguiente

    #Generar con Graphviz la gráfica de la lista
    def graficar_lista(self, archivo):
        with open(f'{archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\trankdir=LR;\n')  #Dibuja el grafo de izquierda a derecha
            file.write('\tlabel="Listado de estudiantes"\n') #Título de la gráfica
            file.write('\tlabelloc = t\n') #Ubicación del título
            file.write('\tnode [shape = record];\n') #Definir características de los nodos, en este caso la forma
            
            # Recorre la lista para agregar los nodos y sus conexiones
            contador = 0
            tmp = self.primero
            while tmp:
                file.write(f'\tnode{contador} [label="{{Codigo: {tmp.get_codigo()}|Titulo: {tmp.get_titulo()}|Autor: {tmp.get_autor()}}}"];\n')
                # file.write(f'\tnode{contador} [label="Codigo: {tmp.codigo}|Titulo: {tmp.titulo}|Autor: {tmp.autor}"];\n')
                if tmp != self.primero:
                    file.write(f'\tnode{contador-1} -> node{contador};\n') #Enlaza el nodo anterior con el nodo actual
                    file.write(f'\tnode{contador} -> node{contador-1};\n') #Enlaza el nodo actual con el nodo anterior
                tmp = tmp.siguiente
                contador += 1
            
            file.write('}')

        os.system("dot -Tsvg "+ archivo +".dot -o "+ archivo +".svg") #Convierte el archivo dot a svg

        #Si se quiere en pdf
        #os.system("dot -Tpdf "+ archivo +".dot -o "+ archivo +".pdf")
