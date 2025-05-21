Edad = int(input("Introduce tu edad: "))
Credencial = input("¿Tienes tu credencial?: ")
if Edad >= 18 and Credencial == "Si":
    print("¡Puedes votar!")
else:
    print("No puedes votar")