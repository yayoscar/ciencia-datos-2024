import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras
    def lanzar_dado(self):
        print(random.randint(1, self.caras))

seis = Dado()
print("Dado de seis caras:")
for i in range(10):
    seis.lanzar_dado()

diez = Dado(10)
print("Dado de diez caras:")
for i in range(10):
    diez.lanzar_dado()

veinte = Dado(20)
print("Dado de veinte caras:")
for i in range(10):
    veinte.lanzar_dado()