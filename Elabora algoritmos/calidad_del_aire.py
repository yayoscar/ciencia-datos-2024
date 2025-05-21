valor = int(input("Ingresa la medición de partículas: "))
if valor <= 99:
    print("Calidad del aire: Bueno")
elif valor <=199:
    print("Calidad del aire: Regular")
elif valor <=299:
    print("Calidad del aire: Alerta")
elif valor <=499:
    print("Calidad del aire: Preemergencia")
else:
    print("Calidad del aire: Superior")
