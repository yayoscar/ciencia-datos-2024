def contar_palabra_en_archivo():
    # Solicitar una palabra al usuario
    palabra = input("Ingresa una palabra para buscar: ").lower()

    try:
        # Abrir y leer el contenido del archivo
        with open("texto.txt", "r") as archivo:
            contenido = archivo.read().lower()

        # Contar cuántas veces aparece la palabra
        cantidad = contenido.count(palabra)

        # Imprimir el resultado
        print(f"La palabra aparece {cantidad} veces.")

    except FileNotFoundError:
        print("El archivo 'texto.txt' no se encontró. Asegúrate de crearlo antes de ejecutar el programa.")

# Ejecutar función
contar_palabra_en_archivo()
