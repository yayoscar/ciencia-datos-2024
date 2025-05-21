def obtener_num_elementos(nombres):
    contar = nombres.split(",")
    return len(contar)

print(obtener_num_elementos("juan,lisa,teresa"))