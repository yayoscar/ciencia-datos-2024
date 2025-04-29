palabras = ['sol', 'luna', 'estrella']
for palabra in palabras:
    nombre_archivo = f"{palabra}.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(palabra)
