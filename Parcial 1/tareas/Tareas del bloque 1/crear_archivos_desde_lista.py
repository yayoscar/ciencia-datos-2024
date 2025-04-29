def crear_archivos_de_palabras():
    palabras = ["sol", "luna", "estrella"]

    for palabra in palabras:
        nombre_archivo = f"{palabra}.txt"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(palabra)

    print("Archivos creados con éxito.")

# Ejecutar función
crear_archivos_de_palabras()
