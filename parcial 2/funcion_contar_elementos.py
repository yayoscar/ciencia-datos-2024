def obtener_num_elementos(cadena):
    elementos = cadena.split(',')
    return len([e.strip() for e in elementos if e.strip()])
print(obtener_num_elementos("juan,lisa, teresa"))
