def incremento(salario,incre):
    resul=((incre/100)*salario)+salario
    print("El incremento a tu salario es: ", resul)
    return
salario=float(input("Ingrese el salraio: "))
incre=float(input("Ingresa el incremento: "))
incremento(salario,incre)
