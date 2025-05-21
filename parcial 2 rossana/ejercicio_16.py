while True:
    num = int(input("Ingrese el numero: "))
    if num <0:
        print("Ingrese un numero valido")
        continue
    factorial = 1
    i = 1
    while i <= num:
        factorial *=i
        i +=1
    print(f"el factorial de {num} es {factorial}")

    break