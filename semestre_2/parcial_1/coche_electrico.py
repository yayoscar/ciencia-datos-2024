from coche import Coche

class Bateria:
    def __init__(self, tamaño_bateria = 75):
        self.tamaño_bateria = tamaño_bateria
    def describir_bateria(self):
        print(f"Este coche tiene una bateria de {self.tamaño_bateria} kWh")

    def obtener_autonomia(self):
        if self.tamaño_bateria == 75:
            autonomia = 260
        elif self.tamaño_bateria == 100:
            autonomia = 315
        print(f"Este coche puede correr aproximadamente {autonomia} millas con una carga completa")

    def mejorar_bateria(self):
        if self.tamaño_bateria != 100:
            self.tamaño_bateria = 100

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def llenar_tanque_gasolina(self):
        print("Este coche no tiene tanque de gasolina")


