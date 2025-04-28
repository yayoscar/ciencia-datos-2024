def contar_caracteres(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            num_caracteres = len(contenido)
            print(f"El archivo {nombre_archivo} tiene {num_caracteres} caracteres.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

contar_caracteres('ensayo.txt')