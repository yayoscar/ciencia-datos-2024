# Lista de palabras
palabras = ["hola", "mundo", "python", "programacion"]

def contar_vocales(palabra):
    contador = 0
    for letra in palabra:
        if letra in 'aeiouAEIOU':
            contador += 1
    return contador

for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {contar_vocales(palabra)} vocales.")