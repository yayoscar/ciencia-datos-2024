import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras

    def lanzar_dado(self):
        print(random.randint(1, self.caras))

d6 = Dado()
for _ in range(10):
    d6.lanzar_dado()

d10 = Dado(10)
for _ in range(10):
    d10.lanzar_dado()

d20 = Dado(20)
for _ in range(10):
    d20.lanzar_dado()
