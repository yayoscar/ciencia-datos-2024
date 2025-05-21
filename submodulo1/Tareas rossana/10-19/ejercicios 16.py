num = int(input("Ingrese el número para calcular el factorial: "))
factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print("El factorial es:", factorial)
