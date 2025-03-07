
"""
Ejercicio: 
* Procesar y Analizar un Archivo de Texto
* Abre un archivo de texto llamado datos.txt.
* Leer el contenido línea por línea y procesa los datos.
* Realizar un análisis del contenido, incluyendo:
* Contar cuántas líneas y palabras hay en total.
* Identificar la línea más larga (en términos de número de palabras).
* Calcular el número promedio de palabras por línea.
* Escribir el resultado en un nuevo archivo llamado analisis.txt.
"""

total_lineas = 0
total_palabras = 0
longitud_maxima = 0
linea_mas_larga = ""
promedio_palabras = 0

#Abrir el archivo en modo 'read'
with open('datos.txt', 'r', encoding='UTF-8') as archivo:
    lineas = archivo.readlines() 
    total_lineas = len(lineas)
    for linea in lineas:
        palabras = linea.split() 
        num_palabras = len(palabras) 
        total_palabras += num_palabras  

        if num_palabras > longitud_maxima:
            longitud_maxima = num_palabras
            linea_mas_larga = linea.strip()

    promedio_palabras = total_palabras / total_lineas if total_lineas > 0 else 0

#Abrir el archivo en modo escritura
with open('analisis.txt', 'w',  encoding='UTF-8') as archivo_analisis:
    archivo_analisis.write(f"Análisis del archivo 'datos.txt':\n")
    archivo_analisis.write(f"Número total de líneas: {total_lineas}\n")
    archivo_analisis.write(f"Número total de palabras: {total_palabras}\n")
    archivo_analisis.write(f"Promedio de palabras por línea: {promedio_palabras:.2f}\n")
    archivo_analisis.write(f"Línea más larga ({longitud_maxima} palabras): {linea_mas_larga}\n")

print("El análisis ha sido escrito en 'analisis.txt'.")
