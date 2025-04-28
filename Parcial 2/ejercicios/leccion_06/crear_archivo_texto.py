def crear_archivo(nombre_archivo, texto):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(texto)
        print(f"Archivo {nombre_archivo} creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

crear_archivo('archivo.txt', 'caracol')