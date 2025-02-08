from clases.estudiante import Estudiante #Importando la clase Estudiante
from clases.profesor import Profesor #Importando la clase Profesor

def menu():
    print(' -----------------------')
    print('|     MENÚ PRINCIPAL    |')
    print(' -----------------------')
    print('|1.Registrar estudiante |')
    print('|2.Registrar profesor   |')
    print('|3.Mostrar listado      |')
    print('|4.Salir                |')
    print(' -----------------------')

if __name__ == '__main__':

    listado = []

    while True:
        menu()
        opcion = input('Ingresa una opción: ')

        if opcion == '1':
            nombre = input('Ingresa el nombre: ')
            edad = input('Ingresa la edad: ')
            carnet = input('Ingresa el carnet: ')

            estudiante = Estudiante(nombre, int(edad), int(carnet))
            listado.append(estudiante)
        elif opcion == '2':
            nombre = input('Ingresa el nombre: ')
            edad = input('Ingresa la edad: ')
            id = input('Ingresa el id: ')
            salario = input('Ingresa el salario: ')

            profesor = Profesor(nombre, int(edad), int(id), salario)
            listado.append(profesor)
        elif opcion == '3':
            for elemento in listado:
                elemento.saludar()
                if isinstance(elemento, Profesor):
                    elemento.describir()
                print()
        elif opcion ==  '4':
            print('Programa finalizado')
            break
        else:
            print('Opción no válida')
