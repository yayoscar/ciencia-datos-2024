def obtener_mensaje_motivacional(opcion):
    if opcion == 1:
        return " La vida tiene muchas cosas que ofrecer, no te desanimes."
    if opcion == 2:
        return "Siéntate y respira, inhala, exhala"
    if opcion == 3:
        return "En medio de la dificultad, se esconde la oportunidad"
    if opcion == 4:
        return "¡Sigue así"
    if opcion == 5:
        return "Está bien que no tengas ganas de hacer nada, tómate un tiempo y piensa lo que harás, no te sientas presionad@"
    if opcion == 6:
        return "Esperamos haberte ayudado"
def mostrar_menu(opcion):
 print("Frases para los siguientes estados emocionales")
print("1. Triste")
print("2. Ansioso/a")
print("3. Cansado/a")
print("4. Feliz")
print("5. Sin ganas de nada")
print("6. Salir")
opcion=input("¿Còmo te sientes hoy? ")
obtener_mensaje_motivacional(opcion)

def motivar():
    continuar = True
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción (1-6): "))
            if opcion == 6:
                print(" Gracias por usar el motivador. ¡Cuídate mucho!")
                continuar = False
            else:
                mensaje = obtener_mensaje_motivacional(opcion)
                print("\n Mensaje para ti:")
                print(mensaje)
        except ValueError:
            print("❗ Por favor, ingresa un número válido del 1 al 6.")

if __name__ == "__main__":
    motivar()
