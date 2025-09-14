class Bateria:
    def __init__(self, capacidad=75):
        self.capacidad = capacidad

    def obtener_autonomia(self):
        autonomia = self.capacidad * 3
        print(f"Autonomía: {autonomia} km")

    def mejorar_bateria(self):
        if self.capacidad < 100:
            self.capacidad = 100
            print("Batería mejorada a 100 kWh")
        else:
            print("La batería ya es de 100 kWh")

class CocheElectrico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = Bateria()

mi_coche = CocheElectrico("Tesla", "Model S")
mi_coche.bateria.obtener_autonomia()
mi_coche.bateria.mejorar_bateria()
mi_coche.bateria.obtener_autonomia()
