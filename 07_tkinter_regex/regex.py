import re

cadena = "hola estudiantes, hola mundo"

#Buscar una palabra específica en una cadena
#Devuelve la primera coincidencia encontrada
print('--------------------------------------')
print('     Buscar primera coincidencia      ')
print('--------------------------------------')
patron = r"hola"
if re.search(patron, cadena):
    print("Se encontró el patrón")
else:
    print("No se encontró el patrón")
print()


#Determinar si una cadena empieza con una palabra específica
print('--------------------------------------')
print('              Empieza con             ')
print('--------------------------------------')
patron = r"^hola"
if re.search(patron, cadena):
    print("La cadena empieza con 'hola'")
else:
    print("La cadena no empieza con 'hola'")
print()


#Buscar si una cadena termina con una palabra específica
print('--------------------------------------')
print('              Termina con             ')
print('--------------------------------------')
patron = r"mundo$"
if re.search(patron, cadena):
    print("La cadena termina con 'mundo'")
else:
    print("La cadena no termina con 'mundo'")
print()


#Encontrar todas las coincidencias en una cadena
patron = r"Python"  # \b es un límite de palabra, \w+ es una palabra
cadena = "Python es un lenguaje interpretado, Python fue lanzado en 1991, python es el lenguaje utilizado en IPC2."
print('--------------------------------------')
print('   Encontrar todas las coincidencias  ')
print('--------------------------------------')
resultados = re.findall(patron, cadena)
print("Coincidencias encontradas:", resultados)
print()


#Dividir una cadena en palabras
print('--------------------------------------')
print('          Dividir una cadena          ')
print('--------------------------------------')
patron = r"\s+"  # \s+ coincide con uno o más espacios en blanco
partes = re.split(patron, cadena)
print("Partes de la cadena:", partes)
print()


#Sustituir todas las ocurrencias de una palabra por otra
print('--------------------------------------')
print('               Sustituir              ')
print('--------------------------------------')
patron = r"mundo"
cadena = "Hola mundo, mundo, mundo!"
print("Cadena antes de la sustitución:", cadena)
nueva_cadena = re.sub(patron, "Python", cadena)
print("Cadena después de la sustitución:", nueva_cadena)
print()

#Coincidencia case insensitive
print('--------------------------------------')
print('   Encontrar todas las coincidencias  ')
print('--------------------------------------')
patron = r"python"
cadena = "Python es un lenguaje interpretado, Python fue lanzado en 1991, python es el lenguaje utilizado en IPC2."
resultados = re.findall(patron, cadena, re.IGNORECASE)
print("Coincidencias encontradas:", resultados)
print()

#####################################################################################################################################

#ER básica para validar direcciones de correo electrónico
print('--------------------------------------')
print('          ER Correo electrónico       ')
print('--------------------------------------')
patron = r"(\w+)@(\w+\.\w+)"
cadena = "correo@example.com"
resultado = re.search(patron, cadena)
if resultado:
    nombre = resultado.group(1)
    dominio = resultado.group(2)
    print(f"Nombre: {nombre}, Dominio: {dominio}")
else:
    print("No se encontró el patrón")
print()


#ER básica para validar números de teléfono
#formato: XXXX-XXXX
print('--------------------------------------')
print('         ER número de teléfono        ')
print('--------------------------------------')
patron = r"^\d{4}-\d{4}$"
telefono = "1234-5678"
if re.match(patron, telefono):
    print("Número de teléfono válido")
else:
    print("Número de teléfono inválido")

#Compilar un patrón y usarlo varias veces
patron_compilado = re.compile(r"\d{4}-\d{4}")
telefonos = ["1234-5678", "9012-3456", "78901234"]
for telefono in telefonos:
    if patron_compilado.match(telefono):
        print(f"El número de teléfono {telefono} es válido")
    else:
        print(f"El número de teléfono {telefono} no es válido")
print()

#ER básica para validar contraseñas
print('--------------------------------------')
print('            ER contraseñas            ')
print('--------------------------------------')
'''
Explicación del patrón:

Al menos una letra minúscula: (?=.*[a-z])
Al menos una letra mayúscula: (?=.*[A-Z])
Al menos un dígito: (?=.*\d)
Longitud mínima de 8 caracteres: [A-Za-z\d]{8,}

?= : Valida si el carácter está presente más adelante en la cadena.
.  : Indica cualquier carácter exceptuando salto de línea.
*  : Cerradura de Kleene, indica cero o más ocurrencias.
'''
patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
if re.match(patron, 'Password12345'):
    print('Contraseña segura')
else:
    print('Contraseña insegura')
