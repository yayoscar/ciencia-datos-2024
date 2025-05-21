def IMC (peso,altura):
    imc = peso/(altura **2)
    return imc
peso = float (input("cual es tu peso? "))
estatura = float (input("cual es tu estatura?"))

resultado = IMC(peso,altura)
print(resultado)

if resultado < 18.5:
    print("bajo peso")
elif resultado > 18.5 and resultado < 24.9:
    print("peso normal")
elif resultado > 25 and resultado < 29.9:
    print("sobrepeso")
elif resultado > 30.0 and resultado < 34.9:
    print("obesidad grado 1")
else:
    print("obesidad grado 2")