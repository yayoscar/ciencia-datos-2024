import random
while True:
    moneda= random.randint(1,2)
    if moneda==1:
        print("rosado")
    else:
        print("morado")
        jugar=input("quieres tirar nuevamente s/n: ")
        if jugar.lower()=="n":
            brak
