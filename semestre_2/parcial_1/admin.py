class Privilegios:
    def __init__(self):
        self.privilegios = ["Puede agregar publicación", "Puede eliminar publicación", "Puede banear usuario"]
    def mostrar_privilegios(self):
        print("Privilegios del Administrador")
        for p in self.privilegios:
            print(p)

class Admin(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña)
        self.privilegios = Privilegios()

    def describir_usuario(self):
        print(f"""Nombre: {self.nombre}
Apellido: {self.apellido}
Correo: {self.correo}
Contraseña: {self.contraseña}
Es Administrador""")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}, eres Administrador!")

