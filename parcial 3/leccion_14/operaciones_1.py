def sumar(num1,num2):
    return  num1 + num2

def restar (num1,num2):
    return num1 - num2

def multiplicar (num1,num2):
    return num1 * num2

def dividir (num1,num2):
    try:
     resultado=num1/num2
     return resultado
    except ZeroDivisionError:
     return "No se puede dividir entre 0"
