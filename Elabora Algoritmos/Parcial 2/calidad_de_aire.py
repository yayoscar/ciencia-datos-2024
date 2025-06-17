medicion = int(input("Ingresa el valor de la medición de particules: "))
if 0 <= medicion <= 99:
    estado = "Bueno"
elif 100 <= medicion <= 199:
    estado = "Regular"
elif 280 <= medicion <= 299:
    estado = "Alerta"
elif 300 <= medicion <= 499:
    estado = "Preemergencia"
else:
    estado = "Emergencia"
print (f"El estado de la calidad del aire es: {estado}.")