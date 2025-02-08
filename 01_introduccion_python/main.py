# Comentario de una línea

'''
    Comentario
    de 
    varias
    líneas
'''

if __name__ == '__main__':
    print("Hola estoy en el main")

    # --- Tipos de datos ---
    a = 1 #int
    b = 1.2 #float
    c = "ipc2" #string
    d = 'otro string' #string
    e = True #boolean
    f = False #boolean

    print('### TIPO DE DATOS ###')
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(d), d)
    print(type(e), e)
    print(type(f), f)


    # --- Casteo de datos ---
    w = int(2.5)
    x = str(1)
    y = float(9)
    z = bool("true")

    print('### CASTEOS ###')
    print(type(w), w)
    print(type(x), x)
    print(type(y), y)    
    print(type(z), z)    


    # --- Operadores aritméticos ---
    suma = 1 + 2
    resta = 10 - 2
    multiplicacion = 6 * 6
    division = 6/2

    print('### OPERACIONES ARITMÉTICAS ###')
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)


    # --- Operadores de comparación ---
    print('### OPERACIONES COMPARATIVAS ###')
    print(1 < 2) # Menor
    print(5 > 2) # Mayor
    print(6 >= 4) # Mayor o igual
    print(3 <= 10) # Menor o igual
    print(1 == 0) # Igual a
    print(9 != 7) # Es diferente de


    # --- Operadores lógicos ---
    #Java | Python
    # &&  |  and
    # ||  |  or
    # !   |  not


    # --- Condicionales ---
    if a > 0:
        print("Soy mayor a 0")
    else:
        print("Soy el 0 o un número negativo")


    # --- ciclo for ---
    for i in range(5):
        print("Estudiante ", i)

    for i in range(1, 5):
        print("Estudiante", i)


    # --- Ciclo while ---
    contador = 0
    while contador < 10:
        print('Contador: ' + str(contador))
        contador += 1
    
    
    # --- Función sin parámetros ---
    def funcion():
        print("Soy una función")

    funcion()

    # --- Función con parámetros
    def funcion2(x, y):
        print("Valor de x: {} \nValor de y: {}".format(x, y))

    funcion2(10, 20)

    # --- Función con return
    def funcion3(a, b):
        return a + b
    
    resultado = funcion3(99, 1)
    print(resultado)

    # --- Listas
    lista = []
    lista.append('b')
    lista.append(True)
    print(lista)

    lista.insert(0, 1)
    print(lista)

    for elemento in lista:
        print(elemento)
