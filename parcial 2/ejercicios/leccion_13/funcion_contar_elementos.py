def obtener_num_elementos(cadena):
    separacion = cadena.split(",")
    return len(separacion)


print(obtener_num_elementos("juan, lisa, teresa"))