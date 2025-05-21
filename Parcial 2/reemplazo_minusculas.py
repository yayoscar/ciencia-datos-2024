def convertir_a_minusculas(texto):
    return texto.lower()

def main():
    print("=== CONVERTIR TEXTO A MINÚSCULAS ===")
    entrada = input("Ingresa un texto: ")
    resultado = convertir_a_minusculas(entrada)
    print("Texto en minúsculas:", resultado)

# Ejecutar el programa
if __name__ == "__main__":
    main()
