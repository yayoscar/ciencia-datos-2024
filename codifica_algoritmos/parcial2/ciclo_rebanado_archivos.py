archivos = ["reporte.txt", "descargas.txt", "éxito.txt", "carpetas.txt"]

for archivo in archivos:
    nombre = archivo[:-4]  # Elimina los últimos 4 caracteres ".txt"
    print(nombre.capitalize()).