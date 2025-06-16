import avanzado

print("Elige una operación: potencia, raiz")
operacion = input("Operación: ").lower()

if operacion == "potencia":
    base = float(input("Base: "))
    exponente = float(input("Exponente: "))
    print("Resultado:", avanzado.potencia(base, exponente))
elif operacion == "raiz":
    numero = float(input("Número: "))
    print("Resultado:", avanzado.raiz(numero))
else:
    print("Operación no válida.")