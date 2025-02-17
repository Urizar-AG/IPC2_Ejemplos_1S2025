import xml.etree.ElementTree as ET #Importar librería ElementTree
from clases.tienda import Tienda  #Importar clase Tienda
from clases.producto import Producto #Importar clase Producto

def leer_inventario(ruta, tiendas):
    tree = ET.parse(ruta) #Parsear el archivo XML
    root = tree.getroot() #Obtener el elemento raíz

    nueva_tienda = None
    for local in root.findall('tienda'): #Encontrar todos los elementos que coinciden con la etiqueta 'tienda'
        nueva_tienda = Tienda(local.get("nombre")) 
        productos = []

        for producto in local.findall('producto'): #Iterar sobre los subelementos
            pasillo = producto.get("pasillo") #Obtener el valor del atributo pasillo
            estante = producto.get("estante")
            nombre_producto = producto.find('nombre').text #Encontrar el primer subelemento 'nombre' y obtener el texto
            stock = int(producto.find('stock').text) 
            productos.append(Producto(nombre_producto, pasillo, estante, stock))

        nueva_tienda.productos = productos
        tiendas.append(nueva_tienda)
    
    print('Información leída con éxito')

def escribir_inventario(ruta, tiendas):
    root = ET.Element("inventario") #Crea el elemento raíz con la etiqueta 'inventario'
    
    for tienda in tiendas:
        elemento_tienda = ET.SubElement(root, 'tienda') #Agrega a la raíz un subelemento 'tienda'
        elemento_tienda.set('nombre', tienda.get_nombre()) #Agrega el atributo 'nombre' al subelemento

        for producto in tienda.productos:
            elemento_producto = ET.SubElement(elemento_tienda, 'producto') 
            elemento_producto.set('pasillo', producto.get_pasillo())
            elemento_producto.set('estante', producto.get_estante())
            
            elemento_nombre = ET.SubElement(elemento_producto, 'nombre')
            elemento_nombre.text = producto.get_nombre() #Agrega el texto al elemento
            elemento_stock = ET.SubElement(elemento_producto, 'stock')
            elemento_stock.text = str(producto.get_stock() + 10)  #Para el ejemplo el único cambio es el aumento del stock

    ET.indent(root, space='\t') #Agrega identación para que se vea mejor
    ET.ElementTree(root).write(ruta, encoding='UTF-8', xml_declaration=True) #Guardar el archivo XML
    