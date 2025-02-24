from lista_simple import ListaSimple

if __name__ == '__main__':
    estudiantes = ListaSimple()
    print('---------- Insertando al final ----------')
    estudiantes.insertar_final(200001234, 'Andrea')
    estudiantes.insertar_final(200004567, 'Juan')
    estudiantes.mostrar_lista()
    print('')

    print('---------- Insertando al inicio ----------')
    estudiantes.insertar_inicio(200008901, 'Pedro')
    estudiantes.insertar_inicio(200002345, 'Carla')
    estudiantes.mostrar_lista()
    print('')

    estudiante = estudiantes.buscar(200001234)
    estudiante.mostrar_info()

    estudiante2 = estudiantes.buscar(201901235) #Este carnet no existe
    if estudiante2:
        estudiante2.mostrar_info()

    estudiantes.graficar_lista('./lista_estudiantes')

    #Elimina el primer nodo 
    estudiantes.eliminar(200002345)
    estudiantes.graficar_lista('lista_estudiantes2')

    #Elimina el último nodo
    estudiantes.eliminar(200004567)
    estudiantes.graficar_lista('lista_estudiantes3')


    # Quitar los comentarios para el ejemplo de la rejilla
    '''
    estudiantes.insertar_final(201200000, 'Carlos')
    estudiantes.insertar_final(201300000, 'Susan')
    estudiantes.insertar_final(201400001, 'Fernanda')
    estudiantes.insertar_final(201500002, 'Alejandra')
    estudiantes.insertar_final(201600003, 'Diego')
    estudiantes.insertar_final(201700004, 'Angel')
    estudiantes.insertar_final(201800005, 'Pedro')
    estudiantes.insertar_final(201900006, 'Emely')
    estudiantes.insertar_final(202000007, 'Mario')
    estudiantes.insertar_final(202100008, 'Hector')
    estudiantes.insertar_final(202200009, 'Rosa')
    estudiantes.insertar_final(202300010, 'Carla')
    estudiantes.insertar_final(202400011, 'Fernando')
    estudiantes.insertar_final(202500011, 'Javier')
    estudiantes.graficar_rejilla('./lista_rejilla', 4, 4)
    '''
