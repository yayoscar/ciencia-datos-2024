print("Para saber si la calidad de aire es buena")
n1=  int( input("Coloca la medida "))
if  n1 <= 99:
    print("El aire es bueno")
elif n1 <=  199:
    print("regular")
elif n1 <= 299:
    print("Alerta")
elif  n1 <= 499:
    print("Preemergencia")
else:
    print("Emergencia")
