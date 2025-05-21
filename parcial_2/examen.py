def leer_temperaturas(ruta_archivo="temperaturas.txt"):
    with open(ruta_archivo, "w") as archivo_local:
        temperatura_local = archivo_local.readlines()
    return temperatura_local
