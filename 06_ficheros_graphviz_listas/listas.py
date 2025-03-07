import graphviz #Importar la librería graphviz -> Instalación pip install graphviz

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
  
    def eliminar(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

    def visualizar(self, nombre_archivo):
        grafo = graphviz.Digraph(format='png')
        grafo.attr(rankdir='LR') #Dirección de la gráfica -> Left to Right
        
        actual = self.cabeza
        while actual:
            #Nodos predeterminados
            grafo.node(str(actual.valor), str(actual.valor))

            #Nodos personalizados
            # grafo.node(str(actual.valor), str(actual.valor), shape='box', style='filled',  color='lightblue',  fillcolor='lightgreen')
            
            if actual.siguiente:
                #Aristas predeterminadas
                grafo.edge(str(actual.valor), str(actual.siguiente.valor))

                #Aristas personalizadas
                # grafo.edge(str(actual.valor), str(actual.siguiente.valor), color='blue', style='dashed')
            actual = actual.siguiente
        grafo.render(nombre_archivo, view=True)

if __name__ == '__main__':
    lista = ListaEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    lista.visualizar('lista_enlazada_inicial')

    lista.agregar(40)
    lista.eliminar(20)
    # Visualizar la lista actualizada
    lista.visualizar('lista_enlazada_actualizada')
