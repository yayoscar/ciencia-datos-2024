paises = ["Albania", "Bélgica", "Croacia", "Dinamarca", "Eslovenia"]
nombres_archivo = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt"]

for pais, nombre_archivo in zip(paises, nombres_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(pais)
        print(f"Archivo {nombre_archivo} creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo {nombre_archivo}: {e}")