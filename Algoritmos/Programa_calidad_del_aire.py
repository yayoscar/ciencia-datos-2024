particulas = int(input("Ingrese la calidad del aire: "))
if particulas >= 0 and particulas <= 99:
    calidad_aire = "Bueno"
elif particulas >= 100 and particulas <= 199:
    calidad_aire = "Regular"
elif particulas >= 200 and particulas <= 299:
    calidad_aire = "Alerta"
elif particulas >= 300 and particulas <= 499:
    calidad_aire = "Preemergencia"
else:
    calidad_aire = "Emergencia"

print(f"La calidad del aire es: {calidad_aire}")












