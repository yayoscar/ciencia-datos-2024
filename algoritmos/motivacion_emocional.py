import random

def obtener_frases_motivacionales(estado_animo):
    frases = {
        "triste": [
            "No estás solo, siempre hay esperanza.",
            "La tristeza es temporal, pero la felicidad es una elección.",
            "Recuerda que cada día es una oportunidad para empezar de nuevo.",
            "No te rindas, cada caída es una lección para levantarte más fuerte.",
            "La vida es un reto, pero también es un regalo."
        ],
        "desanimado": [
            "Puedes hacerlo, solo necesitas creer en ti mismo.",
            "No te desanimes, cada pequeño paso te acerca a tu meta.",
            "La perseverancia es la clave para el éxito.",
            "No importa cuán difícil sea, siempre hay una solución.",
            "Cree en ti mismo y podrás lograrlo."
        ],
        "motivado": [
            "¡Excelente! Estás en el camino correcto.",
            "Sigue adelante, tus metas están cerca.",
            "La motivación es el motor que te lleva al éxito.",
            "Cada logro es un paso más hacia tus sueños.",
            "¡Vamos! Estás haciendo un gran trabajo."
        ],
        "enojado": [
            "Respira profundo y calma esa tempestad.",
            "La ira es una emoción fuerte, pero puedes controlarla.",
            "No dejes que la ira te consuma, busca la paz interior.",
            "La calma es una elección, elige estar tranquilo.",
            "Recuerda que la paciencia es una virtud."
        ]
    }
    return random.choice(frases.get(estado_animo, ["No se ha encontrado frases para ese estado de ánimo."]))

def main():
    print("Bienvenido al programa de frases motivacionales.")
    while True:
        print("\n¿Cómo te sientes hoy?")
        print("1. Triste")
        print("2. Desanimado")
        print("3. Motivado")
        print("4. Enojado")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(obtener_frases_motivacionales("triste"))
        elif opcion == "2":
            print(obtener_frases_motivacionales("desanimado"))
        elif opcion == "3":
            print(obtener_frases_motivacionales("motivado"))
        elif opcion == "4":
            print(obtener_frases_motivacionales("enojado"))
        elif opcion == "5":
            print("Adiós, que tengas un buen día.")
            break
        else:
            print("Opción inválida, por favor elige una opción correcta.")

if __name__ == "__main__":
    main()
