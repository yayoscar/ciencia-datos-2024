def obtener_temperaturas():
 lista=("temparatura")
 input("listas")

temperaturas = obtener_temperaturas()

print(temperaturas)

temperatura=int(input("ingrese la temperatura: "))
if temperatura<18.8:
    print("promedio")
elif 22.7<= temperatura <= 15.3:
    print("minima")
else:
    print("maxima")
