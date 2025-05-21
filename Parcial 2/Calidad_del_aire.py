ica = int(input("Introduce el valor del índice de calidad del aire (ICA) : "))
if ica <= 99:
    print ("La calidad del aire es: Buena")
elif ica <= 199:
    print ("La calidad del aire es: Regular")
elif ica <= 299:
    print ("La calidad del aire es: Alerta ")
elif ica <= 499:
    print ("La calidad del aire es: Preemergencia ")
else:
    print ("La calidad del aire es: Emergencia ")