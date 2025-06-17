texto = "python es un gran lenguaje"
print(texto.capitalize()) # Salida: "Python es un gran lenguaje"


opcion = int(input("Elige una opción (1-3): "))
match opcion:
 case 1:
  print("Seleccionaste la opción 1")
 case 2:
  print("Seleccionaste la opción 2")
 case 3:
  print("Seleccionaste la opción 3")
 case _:
  print("Opción no válida")


while True:
 opcion = input("Escribe 'salir' para terminar: ")
 if opcion.lower() == 'salir':
   break


edad = int(input("Ingrese su edad: "))
if edad >= 18:
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")

try:
    x = int("Hola")
except ValueError:
    print("Error: No es un número válido")


import math
print(math.sqrt(16))  # Salida: 4.0


def suma(a, b):
    return a + b
print(suma(3, 5))  # Salida: 8


def saludo():
    print("Hola")
saludo()


x = 0
while x < 3:
    print("Hola")
    x += 1


for i in range(3):
    print("Hola")


edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


dia = input("Introduce un día de la semana: ")
match dia:
    case "Lunes" | "Martes" | "Miércoles":
        print("Es el comienzo de la semana.")
    case "Jueves" | "Viernes":
        print("¡Casi es fin de semana!")
    case "Sabado" | "Domingo":
        print("¡Fin de semana!")
    case _:
        print("Día de la semana desconocido.")


while True:
    edad = input("Introduce tu edad (o escribe salir para terminar): ")
    if edad.lower()== "salir":
        break
    try:
        edad = int(edad)
        if edad < 0:
            print("Edad inválida. Introduce un número positivo.")
        else:
            print(f"Tu edad es '{edad}'.")
            break
    except ValueError:
        print("Entrada inválida. Intrpoduce un número o 'salir'.")


cadena = input("Introduce una cadena: ")
for i, caracter in enumerate(cadena):
    print(f"El carácter '{caracter}' está en la posición {i}")


frase = input("Introduce una frase: ")
palabra = input("Introduce una palabra: ")
if palabra in frase:
    print(f"La palabra '{palabra}' está en la frase.")
else:
    print(f"La palabra '{palabra}' no está en la frase.")


num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa el segundo número: "))
suma = num1 + num2
print(f"La suma es: {suma}")