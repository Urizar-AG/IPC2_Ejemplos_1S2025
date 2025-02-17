from xml.dom import minidom #Importar librería Minidom
from clases.tienda import Tienda  #Importar clase Tienda
from clases.producto import Producto #Importar clase Producto

def leer_inventario(ruta, tiendas):
    doc = minidom.parse(ruta) #Parsear el archivo

    nueva_tienda = None
    for local in doc.getElementsByTagName('tienda'): #Iterar sobre todos los elementos con la etiqueta 'tienda'
        nueva_tienda = Tienda(local.getAttribute('nombre')) 
        productos = []

        for producto in local.getElementsByTagName('producto'): #Iterar sobre los subelementos
            pasillo = producto.getAttribute('pasillo') #Obtener el valor del atributo pasillo
            estante = producto.getAttribute('estante')
            nombre_producto = producto.getElementsByTagName('nombre')[0].firstChild.data #Encontrar el primer subelemento 'nombre' y obtener el texto
            stock = int(producto.getElementsByTagName('stock')[0].firstChild.data)
            productos.append(Producto(nombre_producto, pasillo, estante, stock))

        nueva_tienda.productos = productos
        tiendas.append(nueva_tienda)

    print('Información leída con éxito')

def escribir_inventario(ruta, tiendas):
    doc = minidom.Document() #Crea el documento DOM
    root = doc.createElement('inventario') #Crea el elemento raíz con la etiqueta inventario
    doc.appendChild(root) #Agrega la raíz al documento


    for tienda in tiendas:
        elemento_tienda = doc.createElement('tienda') #Crea el elemento tienda
        elemento_tienda.setAttribute('nombre', tienda.get_nombre()) #Agregar el atributo 'nombre' al elemento

        for producto in tienda.productos:
            elemento_producto = doc.createElement('producto') 
            elemento_producto.setAttribute('pasillo', producto.get_pasillo())
            elemento_producto.setAttribute('estante', producto.get_estante())

            elemento_nombre = doc.createElement('nombre')
            elemento_nombre.appendChild(doc.createTextNode(producto.get_nombre())) #Agrega el subelemento 'nombre' y su texto
            elemento_producto.appendChild(elemento_nombre) #Agrega el subelemento al elemento 'producto'
            
            elemento_stock = doc.createElement('stock')
            elemento_stock.appendChild(doc.createTextNode(str(producto.get_stock() + 15))) #Para el ejemplo el único cambio es el aumento del stock
            elemento_producto.appendChild(elemento_stock)

            elemento_tienda.appendChild(elemento_producto)

        root.appendChild(elemento_tienda)

    #Guardar el archivo XML
    with open(ruta, 'wb') as file:
        file.write(doc.toprettyxml(indent='\t', encoding="UTF-8")) 
