import xml_elementtree as xmlet 
import xml_minidom as xmldom

def menu():
    print("+------------------------------------+")
    print("|             MENÚ PRINCIPAL         |")
    print("+------------------------------------+")
    print("|1. Limpiar sistema                  |")
    print("|2. Leer archivo con ElementTree     |")
    print("|3. Leer archivo con Minidom         |")
    print("|4. Mostrar inventario               |")
    print("|5. Escribir archivo con ElementTree |")
    print("|6. Escribir archivo con Minidom     |")
    print("|7. Salir                            |")
    print("+------------------------------------+")

    opcion = int(input('Ingresa una opción: '))
    return opcion

if __name__ == "__main__":

    tiendas = []
    ruta = 'inventario.xml'

    while True:
        opc = menu()
        if opc == 1:
            tiendas = []
        elif opc == 2: 
            #Se puede preguntar al usuario por la ruta
            # ruta = input('Ingresa la ruta del archivo: ') 

            xmlet.leer_inventario(ruta, tiendas)
            print('')
        elif opc == 3:
            xmldom.leer_inventario(ruta, tiendas)
            print('')
        elif opc == 4:
            for tienda in tiendas:
                print('====================================')
                print(tienda.get_nombre())
                print('====================================')
                for producto in tienda.productos:
                    producto.get_detalles()   
                    print('')
        elif opc == 5:
            xmlet.escribir_inventario('inventario_elementtree.xml', tiendas)
            print('')
        elif opc == 6:
            xmldom.escribir_inventario('inventario_minidom.xml', tiendas)
            print('')
        elif opc == 7:
            print('Programa finalizado')
            break
        else:
            print('Opción no válida\n')
