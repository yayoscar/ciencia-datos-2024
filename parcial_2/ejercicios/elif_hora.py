hora = int(input("Qué hora es? "))
if hora <= 12:
    print("buenos días")
elif hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")