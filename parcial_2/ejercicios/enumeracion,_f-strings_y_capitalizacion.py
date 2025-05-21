nombres_archivos = ['documento', 'informe', 'presentación']
for indice, elemento in enumerate(nombres_archivos):
    elemento = elemento.capitalize()
    print(f"{indice}-{elemento}.txt")