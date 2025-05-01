temperatura = int(input("Ingrese la temperatura:"))
''' NO OPTIMIZADO:
if temperatura < 15:
    print("Hace frío")
elif 15 <= temperatura <= 25:
    print("Clima agradable")
else:
    print("Hace calor")'''
#OPTIMIZADO:
if temperatura < 15:
    print("Hace frío")
elif temperatura > 25:
    print("Hace calor")
else:
    print("Clima agradable")