# Lista de nombres de archivos
nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']

# Iterar sobre la lista y crear archivos
for nombre in nombres_archivo:
    try:
        # Abrir archivo en modo escritura y escribir "Hola"
        with open(nombre, 'w') as archivo:
            archivo.write('Hola')
        print(f"Archivo {nombre} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo {nombre}: {e}")