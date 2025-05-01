tiene_coche = input("¿Tienes coche? ")
if tiene_coche == "si":
    tiene_coche = True
if tiene_coche == True:
    tiene_gasolina = input("¿Tiene gasolina? ")
    if tiene_gasolina == "si":
        tiene_gasolina = True
    if tiene_gasolina == True:
        print("Listo para salir")
    else:
        print("Necesita gasolina")
else:
    print("Que mal")