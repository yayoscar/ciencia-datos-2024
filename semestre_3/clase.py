class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        print(f"El perro {self.nombre} se ha sentado")

    def dar_vuelta(self):
        print(f"El perro {self.nombre} se dio la vuelta")

mi_perro = Perro('Oreo','5')
print(f"El nombre de mi perro es {mi_perro.nombre}")
print(f"La edad de mi perro es {mi_perro.edad}")
mi_perro.sentarse()
mi_perro.dar_vuelta()
tu_perro = Perro('Pacho','15')
print(f"El nombre de mi perro es {tu_perro.nombre}")
print(f"La edad de mi perro es {tu_perro.edad}")
tu_perro.sentarse()
tu_perro.dar_vuelta()