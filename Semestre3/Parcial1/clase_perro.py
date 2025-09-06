class Perro:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def sentarse(self):
            print(f"El perro {self.nombre} se ha sentado")
    def dar_vuelta(self):
            print(f"El perro {self.nombre} a dado una vuelta")

Pastor=Perro('Bobi',16)

print(f"El nombre de mi perro es {Pastor.nombre}")
print(f"La edad de mi perro es {Pastor.edad}")
Pastor.sentarse()
Pastor.dar_vuelta()

Tu_perro=Perro('Rocky', 3)

print(f"El nombre de tu perro es {Tu_perro.nombre}")
print(f"La edad de tu perro es {Tu_perro.edad}")
Tu_perro.sentarse()
Tu_perro.dar_vuelta()