archivos = ['parcial 2/ejercicios/a.txt',
            'parcial 2/ejercicios/b.txt',
            'parcial 2/ejercicios/c.txt']

for archivo in archivos:
    with open(archivo, encoding='utf-8') as f:
        contenido = f.read()
        print(contenido)
