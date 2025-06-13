def interes_simple(c,r,t):
    interes =  c * r/100 * t
    return interes

def interes_compuesto(capital,tasas,tiempo):
    interes_total = 0
    h=capital
    for año in range (tiempo):
        interes = h*(tasas/100)
        interes_total += interes
        return interes_total

c = input("Ingrese su capital de ingresos: ")
r =input("Ingrese la tasa de interes: ")
t =input("Ingresen el tiempo estimado: ")
k = input("Ingrese el tiempo en años en el que va a sacar su dinero: ")
tipo_interes = input("Ingrese el tipo de interes que desea calcular: ")
if tipo_interes == 'simple':
    print(interes_simple(c,r,t))
else:
    print(interes_compuesto(c,r,k,t))

