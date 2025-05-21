def obtener_num_elementos(nombres):
    lissta = nombres.split(',')
    return len(lissta)


print(obtener_num_elementos("juan, lisa, teresa"))