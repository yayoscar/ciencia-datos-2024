def funcion_contar_argumentos(nombres):
    lista = nombres.split(",")
    return len(lista)

print(funcion_contar_argumentos("juan,lisa,teresa"))