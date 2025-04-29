palabras = ["palabra1", "palabra2", "palabra3"]

for palabra in palabras:
    try:
        with open(palabra + ".txt", "w") as archivo:
            archivo.write(palabra)
        print(f"Archivo '{palabra}.txt' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el archivo '{palabra}.txt': {e}")