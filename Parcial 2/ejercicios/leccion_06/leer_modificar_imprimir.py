def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            palabras_procesadas = [palabra.capitalize() for palabra in palabras]
            contenido_actualizado = ' '.join(palabras_procesadas)
            print(contenido_actualizado)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

procesar_archivo('ensayo.txt')