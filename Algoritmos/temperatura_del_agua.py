Temperatura = int(input("Ingrese la temperatura del agua: "))
if Temperatura <= 0:
   print("El agua esta en estado sólido")
elif 0 <Temperatura <100:
    print("El agua esta en estado líquido")
else:
    print("Error")


