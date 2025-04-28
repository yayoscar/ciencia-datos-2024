def buscar_palabra_en_archivo():
    palabra = input("ingrese una palabra: ").lower()
    try:
        with open("texto.txt","r") as archivo:
            texto = archivo.read().lower()
            conteo = texto.count(palabra)
            print(f"la palabra '{palabra}' aparece {conteo} veces.")
    except FileNotFoundError:
        print("el archivo 'texto.txt' no existe")
buscar_palabra_en_archivo()