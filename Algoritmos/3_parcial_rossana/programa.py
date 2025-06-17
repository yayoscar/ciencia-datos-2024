def calcular_interes_simple(c, ts, t):
 interes = c * (ts/100) * t
 return interes

def compuesto(c, ts, t):
 for i in range(t):
    monto = monto + (monto * (ts/100))
 return monto

print("calculadora de interesses")
print("1. interes simple")
print("2. interes compuesto")

c = float(input("ingresa el capital inicial: "))
ts = float(input("ingresa la tasa de interes: (en %):"))
t = int(input("ingresa el tiempo(en años): "))

opcion = int(input("selecciona la opcion que deseas calcular(1 o 2):" ))
if opcion == 1:
    interes = calcular_interes_simple(c, ts, t)
    print(f"el interes simple generado es:{interes:.2f}")
    print("la cantidad total es: ", interes + c)
elif opcion == 2:
    interes = compuesto(c, ts, t)
    print(f"el interes compuesto generado es:{interes:.2f}")
else:
        print("eleccion no valida. por favor, seleccione 1 o 2.")
