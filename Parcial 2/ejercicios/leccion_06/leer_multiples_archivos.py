# Lista de nombres de archivos
nombres_archivo = ['a.txt', 'b.txt', 'c.txt']

# Iterar sobre la lista y leer archivos
for nombre in nombres_archivo:
    try:
        # Abrir archivo en modo lectura y leer contenido
        with open(nombre, 'r') as archivo:
            contenido = archivo.read().strip()  # Leer y eliminar espacios en blanco
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre} no existe.")
    except Exception as e:
        print(f"Error al leer el archivo {nombre}: {e}")