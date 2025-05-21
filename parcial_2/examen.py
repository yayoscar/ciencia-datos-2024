def extraer_nombre_archivo(lista_todo):
    archivos = []
    for lista in lista_todo:
        for item in lista:
            if item.endswith('txt'):
                archivos.append(item)
    for nombre in archivos:
        nombre = nombre.capitalize()
    return f"Archivos: {archivos}"


def promedio(lista):
    return f"Promedio: {sum(lista)/ len(lista)}"


lista_temps = []
lista_todo = []
with open('temperaturas.txt') as archivo:
    lineas = archivo.readlines()
for linea in lineas:
    arreglo = linea.split('|')
    lista_todo.append(arreglo)
for lista in lista_todo:
    indice = 1
    temp = float(lista[indice])
    indice +=3
    lista_temps.append(temp)
print(promedio(lista_temps))
print(f"Máxima: {max(lista_temps)}")
print(f"Mínima: {min(lista_temps)}")
print(extraer_nombre_archivo(lista_todo))