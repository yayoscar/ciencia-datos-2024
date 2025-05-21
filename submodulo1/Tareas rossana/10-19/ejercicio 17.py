import random
while True:
    moneda = random.randint(1,2)
    if moneda ==1:
        print("Aguila")
    else:
        print("Sol")
    jugar = input("Quieres lanzar de nuevo s/n")
    if jugar.lower()=="n":
        break