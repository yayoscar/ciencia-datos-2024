from matematicas import sumar,restar,multiplicar,division

duda = input("""Que desea realizar?: 
1.sumar
2.restar
3.multiplicacion
4.division """)
while True:
    match duda:
        case "1":
            numero1 = float(input("Ingrese el primer numero a sumar: "))
            numero2 = float(input("Ingresa el segundo numero a sumar: "))
            print("El resultado de la suma",sumar(numero1,numero2))
        case "2":
            numeroa = float(input("Ingrese el primer numero a restar:"))
            numerob = float(input("Ingrese el segundo numero:"))
            print("El resultado de la resta es:",restar(numeroa,numerob))
        case "3":
            numeroe = float(input("Ingrese el primer numero a multiplicar:"))
            numeroi = float(input("Ingrese el segundo numero:"))
            print("El resultado de la multiplicacion es:",multiplicar(numeroe,numeroi))
        case "4":
            numeroc = float(input("Ingrese el primer numero a dividir:"))
            numerod = float(input("Ingrese el segundo numero:"))
            print("El resultado de la division es:", division(numeroc,numerod))
    pregunta = input("Quieres seguir calculando?:")
    if pregunta.lower() == "si":
        continue
    else:
        break