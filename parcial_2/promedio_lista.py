def calcular_promedio(lista):
    if len(lista) == 0:
        return "La lista está vacia. "
    return sum(lista) / len(lista)


mi_lista = [1,2,3,4]
promedio = calcular_promedio(mi_lista)
print("El promedio es: ", promedio)