#Define una función que reciba una lista como un argumento, retorne el valor promedio de los elementos de la lista, por ejemplo, si tu funcion con foo([10, 20, 30, 40)], deberia retornar 25 que es el promedio de esos numeros
def sacar_promedio(lista):
    promedio_lista = sum(lista) / len(lista)
    return promedio_lista

cal = [10, 20, 30, 40]

print(sacar_promedio(cal))
