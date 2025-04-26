def suma(niños):
    res1 = niños[0] + niños[5]
    res2 = niños[1] + niños[4]
    res3 = niños[2] + niños[3]
    return res1, res2, res3
def resta(niños):
    res1 = niños[0] - niños[5]
    res2 = niños[1] - niños[4]
    res3 = niños[2] - niños[3]
    return res1, res2, res3
def multiplicacion(niños):
    res1 = niños[0] * niños[5]
    res2 = niños[1] * niños[4]
    res3 = niños[2] * niños[3]
    return res1, res2, res3
def division(niños):
    res1 = niños[0] / niños[5]
    res2 = niños[1] / niños[4]
    res3 = niños[2] / niños[3]
    return res1, res2, res3
import random; random.randint(1, 10)
indice = 0
niños = [0, 0, 0, 0, 0, 0]
for niño in niños:
    num = random.randint(1, 10)
    niños[indice] = num
    indice +=1
print(f"Estos son los números de los niños : {niños}")
print("""1 = Suma
2 = Resta
3 = Multilplicación
4 = División""")
operacion = int(input("Elige un operador del 1-4: "))
match operacion:
    case 1:
        print(suma(niños))
    case 2:
        print(resta(niños))
    case 3:
        print(multiplicacion(niños))
    case 4:
        print(division(niños))
    case _:
        print("No")