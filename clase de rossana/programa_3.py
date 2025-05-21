aire = int(input("aEscribe la calidad del aire"))
if aire >= 0 and aire<= 99:
    print("la calidad del aire es bueno")
if aire >= 100 and aire <= 199:
    print("la calidad del aire es regular")
if aire >= 200 and aire <= 299:
    print("la calidad del aire es alerta")
if aire >= 300 and aire <= 499:
    print("la calidad del aire es preemergencia")
else:
    print("la calidad del aire es emergencia")
