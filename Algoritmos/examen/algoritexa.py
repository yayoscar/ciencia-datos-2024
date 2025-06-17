def calculo_numero(n1, n2):
    numero= n1 * n2
    return numero

def eleve_numero(n1, n2):
    resultado1=n1**3
    resultado2=n2**3
    return resultado1, resultado2

while True:
 n1= float(input("introduce numero uno:"))
 n2= float(input("introduce numero dos: "))
 resultado1= calculo_numero(n1, n2)
 print("el resultado de la multiplicacion es: ", resultado1)
 resultado2= eleve_numero(n1, n2)
 print("el resultado del cubo es: ", resultado2)
 input("desea repetir con los calculos?:si/no ")










