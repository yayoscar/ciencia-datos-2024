paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]

for pais in paises:
    nombre_archivo = pais + ".txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(pais)
        print(f"Archivo {nombre_archivo} creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo {nombre_archivo}: {e}")