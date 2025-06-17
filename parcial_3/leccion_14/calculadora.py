from opercaiones_1 import sumar,restar,multiplicar,dividir

opcion = input("Que accion desea realizar: ")
match opcion:
    case "sumar":
        num1 = input("ingrese un número: ")
        num2 = input("ingrese otro número: ")
        print(sumar(num1,num2))
    case "restar":
        num1 = input("ingrese un número: ")
        num2 = input("ingrese otro número: ")
        print(restar(num1,num2))
    case "multiplicar":
        num1 = input("ingrese un número: ")
        num2 = input("ingrese otro número: ")
        print(multiplicar(num1,num2))
    case "dividir":
        num1 = input("ingrese un número: ")
        num2 = input("ingrese otro número: ")
        print(dividir(num1,num2))