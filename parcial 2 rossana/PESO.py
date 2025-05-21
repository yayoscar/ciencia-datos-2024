def imc(peso,estatura):
    return peso/(estatura**2)
peso=float(input("ingresa tu peso en kilogramos: "))
estatura=float(input("ingresa tu estatura en metros: "))
print(imc(peso, estatura))
if imc (peso,estatura) <18.5:
    print("bajo peso")
elif imc(peso, estatura) <24.9:
    print("peso normal")
elif imc(peso, estatura) <29.9:
    print("sobre peso")
else:
    print("obesidad")


