def calcular_imc(peso,estatura):
    imc = peso / (estatura ** 2)
    return imc
def clasificar_imc(imc):
    if imc < 18.5:
        return "brazo de 15"
    elif imc < 25:
        return "peso normmal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obecidad"

peso = float(input("ingrese su peso en kilogramos"))
estatura = float(input("ingrese estatura en metros"))
imc = calcular_imc(peso,estatura)
clasificacion = clasificar_imc(imc)
print(f"su imc es: {imc:.2f}")
print(f"clasificacion:{clasificacion}")


