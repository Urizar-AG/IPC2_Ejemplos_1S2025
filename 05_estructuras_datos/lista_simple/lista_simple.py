import os

class Nodo:
    def __init__(self, carnet, nombre):
        #Datos
        self.__carnet = carnet
        self.__nombre = nombre

        #Apuntador al siguiente nodo
        self.siguiente = None

    def get_carnet(self):
        return self.__carnet
    
    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        print(f'Carnet: {self.__carnet} - Nombre: {self.__nombre}')

class ListaSimple:
    def __init__(self):
        self.primero = None #Referencia al primer nodo de  la lista (head)
        # self.length = 0 #Este atributo es opcional, puede ser útil si se requiere llevar el tamaño de la lista

    #Insertar nodo al inicio de la lista
    def insertar_inicio(self, carnet, nombre):
        nuevo = Nodo(carnet, nombre)
        if self.primero is None: #La lista está vacía
            self.primero = nuevo
        else: #Hay por lo menos un nodo en la lista
            nuevo.siguiente = self.primero
            self.primero = nuevo #Mueve el apuntador al nuevo primer nodo de la lista
        # self.length += 1

    #Insertar nodo al final de la lista
    def insertar_final(self, carnet, nombre):
        nuevo = Nodo(carnet, nombre) # Instanciar un nuevo nodo
        if self.primero is None: #La lista está vacía
            self.primero = nuevo
        else: #Hay por lo menos un nodo en la lista
            tmp = self.primero #Nodo auxiliar para recorrer la lista
            while tmp.siguiente is not None:
                tmp = tmp.siguiente #tmp ahora es el nodo siguiente
            tmp.siguiente = nuevo
        # self.length += 1

    #Obtiene un nodo de la lista
    def buscar(self, carnet):
        tmp = self.primero #Nodo auxiliar para recorrer la lista
        while tmp:
            if tmp.get_carnet() == carnet:
                return tmp
            tmp = tmp.siguiente
        return None #No encontro el carnet retorna nulo
    
    #Eliminar un nodo de la lista
    def eliminar(self, carnet):
        if self.primero is None:
            print('La lista está vacía')
        elif self.primero.get_carnet() == carnet: #El nodo a eliminar es el primero en la lista
            tmp = self.primero
            self.primero = tmp.siguiente #Primero ahora apunta al segundo nodo
            tmp.siguiente = None
            # self.length -= 1
            print('Nodo eliminado correctamente')
        else:
            prev = self.primero #Nodo anterior al que se está borrando
            tmp = self.primero.siguiente #Nodo a borrar
            while tmp:
                if tmp.get_carnet() == carnet:
                    prev.siguiente = tmp.siguiente
                    tmp.siguiente = None
                    # self.length -= 1
                    print('Nodo eliminado correctamente')
                    return
                prev = tmp 
                tmp = tmp.siguiente

            print('No fue posible eliminar, el carnet no existe')

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
            file.write('\tlabelloc = t') #Ubicación del título
            file.write('\tnode [shape = record];\n') #Definir características de los nodos, en este caso la forma
            
            # Recorre la lista para agregar los nodos y sus conexiones
            contador = 0
            tmp = self.primero
            while tmp:
                file.write(f'\tnode{contador} [label="{{Carnet: {tmp.get_carnet()}|Nombre: {tmp.get_nombre()}}}"];\n')
                if tmp != self.primero:
                    file.write(f'\tnode{contador-1} -> node{contador};\n') #Enlaza el nodo anterior con el nodo actual
                tmp = tmp.siguiente
                contador += 1
            
            file.write('}')

        os.system("dot -Tsvg "+ archivo +".dot -o "+ archivo +".svg")

    #Representar la lista enlazada como una rejilla
    def graficar_rejilla(self, archivo, filas, columnas):
        with open(f'{archivo}.dot', 'w') as file:
            file.write('digraph G {\n')
            file.write('\tlabel="Listado estudiantes\\nRepresentacion de la lista como rejilla"\n')
            file.write('\tlabelloc=t;\n') #Posiciona el título en la parte superior(top)
            file.write('\tnode [shape=plaintext]\n')

            #Creación del nodo
            file.write('\tnode0 [label=<\n') 
            file.write('\t\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">\n')

            #Fila encabezado para los números de columna
            file.write('\t\t\t<TR>\n')
            file.write('\t\t\t\t<TD BORDER="0"></TD>\n')
            for j in range(1, columnas+1):
                file.write(f'\t\t\t\t<TD BORDER="0">{j}</TD>\n') #Número de columna
            file.write('\t\t\t</TR>\n')

            #Agregando los valores por filas
            tmp = self.primero
            for i in range(1, filas+1):
                file.write('\t\t\t<TR>\n')
                file.write(f'\t\t\t\t<TD BORDER="0" CELLPADDING="15">{i}</TD>\n') #Número de fila
                #Contenido de la celda
                for j in range(columnas):
                    file.write(f'\t\t\t\t<TD>{tmp.get_carnet()}</TD>\n') #Contenido de la celda
                    tmp = tmp.siguiente
                file.write('\t\t\t</TR>\n')

            file.write('\t\t</TABLE>>];\n')
            file.write('}')

        os.system("dot -Tsvg "+ archivo +".dot -o "+ archivo +".svg") #Convierte el archivo dot a svg

        #Si se quiere en pdf
        #os.system("dot -Tpdf "+ archivo +".dot -o "+ archivo +".pdf")
