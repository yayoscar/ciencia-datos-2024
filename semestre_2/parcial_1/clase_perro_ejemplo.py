class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def sentarse(self):
        print(f"El perro {self.nombre} se ha sentado")
    def dar_vuelta(self):
        print(f"El perro {self.nombre} se ha dado vuelta")


mi_perro = Perro("Bobi", 4)
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años")
mi_perro.sentarse()
mi_perro.dar_vuelta()
tu_perro = Perro("Tobi", 2)
print(f"El nombre de tu perro es {tu_perro.nombre} y tiene {tu_perro.edad} años")
tu_perro.sentarse()
tu_perro.dar_vuelta()