class Privilegios:
    def __init__(self, privilegios=None):
        self.privilegios = privilegios if privilegios else []

    def mostrar_privilegios(self):
        print("Privilegios:")
        for p in self.privilegios:
            print(f"- {p}")

class Admin:
    def __init__(self, nombre, apellido, privilegios=None):
        self.nombre = nombre
        self.apellido = apellido
        self.privilegios = Privilegios(privilegios)
