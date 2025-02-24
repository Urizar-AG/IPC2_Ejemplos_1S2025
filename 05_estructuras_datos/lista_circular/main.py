from lista_circular import ListaCircular


if __name__ == "__main__":
    lista = ListaCircular()

    lista.insertar_inicio(2)
    lista.insertar_inicio(1)
    lista.insertar_final(3)
    lista.insertar_final(4)
    
    lista.mostrar_lista()
    lista.graficar_lista('./lista_circular')
