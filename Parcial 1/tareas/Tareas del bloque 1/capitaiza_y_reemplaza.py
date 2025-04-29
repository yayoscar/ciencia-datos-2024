def procesar_frase():
    # Pedir al usuario una frase
    frase = input("Ingresa una frase: ")

    # Capitalizar cada palabra
    frase_capitalizada = frase.title()

    # Reemplazar espacios con guiones bajos
    frase_formateada = frase_capitalizada.replace(" ", "_")

    # Imprimir resultado
    print("Frase procesada:", frase_formateada)

# Ejecutar función principal
procesar_frase()
