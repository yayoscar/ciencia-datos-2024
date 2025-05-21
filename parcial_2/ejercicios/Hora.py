hora = int(input("Introuce la hora: "))
if hora < 12:
    print("Buenos días")
if hora < 18:
    if hora >= 12:
        print("Buenas tardes")
else:
    print("Buenas noches")