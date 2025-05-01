edad = int(input("Ingresa tu edad: "))
positivo = "Puedes votar"
negativo = "No puedes votar"
credencial = input("¿Tienes credencial? ")
if credencial == "si"| "Sí"|"sí"|"Si":
    credencial = True
else:
    credencial = False
if edad >= 18 and credencial == True:
    print(positivo)
else:
    print(negativo)