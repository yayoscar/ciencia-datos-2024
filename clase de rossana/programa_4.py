temperatura = input(input("ingrese la temperatura del agua en gtrados celsius"))
if temperatura <= 0:
    print("esta completa")
elif temperatura <= 100:
    print("el agua esta normal")
else:
    print("el agua esta templada")
