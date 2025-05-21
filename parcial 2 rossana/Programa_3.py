calidad= int(input("ingrese la calidad del aire: "))
if calidad<=99:
    print("el aire es bueno")
elif calidad<=199:
    print("el aire esta regular")
elif calidad<=299:
    print("ALERTA")
elif calidad <= 499:
    print("premergencia")
else:
    print("emergenciaaaa")
