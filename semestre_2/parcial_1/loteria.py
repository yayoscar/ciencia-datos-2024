import random
lotería = [1,'e','y',6,'x','v','a',2,3,4,5,7,8,9,0]
ganador = random.choices(lotería, k=4)
mi_boleto = [4, 'e', 'y', 2]
i = 1
while mi_boleto != ganador:
    print(f"El boleto ganador será el que coincida con:{ganador}")
    ganador = random.choices(lotería, k=4)
    i +=1
print(f"Ganaste con {mi_boleto}, tuviste que intentar: {i} veces")