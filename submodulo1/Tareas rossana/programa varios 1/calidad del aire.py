pm10 = float(input("Ingrese el valor de PM10: "))

if pm10 <= 50:
    print("Calidad del aire: Buena")
elif pm10 <= 100:
    print("Calidad del aire: Moderada")
elif pm10 <= 150:
    print("Calidad del aire: No saludable para grupos sensibles")
elif pm10 <= 200:
    print("Calidad del aire: No saludable")
elif pm10 <= 300:
    print("Calidad del aire: Muy no saludable")
else:
    print("Calidad del aire: Peligrosa")
