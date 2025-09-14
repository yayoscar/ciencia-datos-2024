import random

elementos = [1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E"]
mi_boleto = random.sample(elementos, 4)
intentos = 0

while True:
    intento = random.sample(elementos, 4)
    intentos += 1
    if intento == mi_boleto:
        break

print(f"Tu boleto ganó después de {intentos} intentos")
