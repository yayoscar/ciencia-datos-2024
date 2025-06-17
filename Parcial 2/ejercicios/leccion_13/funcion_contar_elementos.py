def obtener_num_elementos(nombres):
    lista = nombres.split(",")
    return len(lista)

print(obtener_num_elementos("juan, lisa, teresa"))