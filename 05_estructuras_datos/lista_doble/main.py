from lista_doble import ListaDoble


if __name__ == '__main__':
    libros = ListaDoble()
    libros.insertar_inicio(1234, 'Frankenstein', 'Mary Shelley')
    libros.insertar_final(5678, 'La Metamorfosis', 'Franz Kafka')
    libros.insertar_final(9012, 'El Principito', 'Antoine de Saint-Exupery')

    libros.mostrar_lista()
    libros.graficar_lista('./listado_libros')
