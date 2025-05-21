temperatura= int(input("En que temperatura esta el agua? "))
if temperatura<=0:
    print("El agua esta congelado")
elif temperatura<=100:
    print("El agua esta evaporado")
else:
    print("El Agua esta liquido")