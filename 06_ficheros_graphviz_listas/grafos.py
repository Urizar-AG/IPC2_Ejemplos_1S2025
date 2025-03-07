import graphviz #Importar la librería graphviz -> Instalación pip install graphviz

# Ejemplo 1: Crear un Grafo No Dirigido
grafo = graphviz.Graph(format='png')  #Se puede cambiar el formato a 'pdf', 'svg', etc.
grafo.node('A', 'Nodo A')
grafo.node('B', 'Nodo B')
grafo.node('C', 'Nodo C')

# Agregar aristas (conexiones) entre los nodos
grafo.edge('A', 'B')
grafo.edge('B', 'C')
grafo.edge('A', 'C')

# Renderizar y guardar el grafo no dirigido
grafo.render('grafo_no_dirigido', view=True)  # 'view=True' abre el grafo en el visor predeterminado

# Ejemplo 2: Crear un Grafo Dirigido
grafo_dirigido = graphviz.Digraph(format='png')
grafo_dirigido.node('A', 'Inicio')
grafo_dirigido.node('B', 'Proceso')
grafo_dirigido.node('C', 'Fin')

# Agregar aristas dirigidas
grafo_dirigido.edge('A', 'B')
grafo_dirigido.edge('B', 'C')
grafo_dirigido.edge('A', 'C')

# Renderizar y guardar el grafo dirigido
grafo_dirigido.render('grafo_dirigido', view=True)

# Ejemplo 3: Crear un Grafo Dirigido con Nodos y Aristas Personalizadas
grafo_personalizado = graphviz.Digraph(format='png')
grafo_personalizado.node('A', 'Nodo A', shape='box', color='red')
grafo_personalizado.node('B', 'Nodo B', shape='ellipse', color='blue')
grafo_personalizado.node('C', 'Nodo C', shape='diamond', color='green')

# Agregar aristas personalizadas
grafo_personalizado.edge('A', 'B', label='Arista 1', color='purple')
grafo_personalizado.edge('B', 'C', label='Arista 2', style='dashed')
grafo_personalizado.edge('A', 'C', label='Arista 3', style='dotted')

# Renderizar y guardar el grafo personalizado
grafo_personalizado.render('grafo_personalizado', view=True)
