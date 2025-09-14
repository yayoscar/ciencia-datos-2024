class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Admin(Usuario):
    def __init__(self, nombre, apellido, privilegios=None):
        super().__init__(nombre, apellido)
        self.privilegios = privilegios if privilegios else []

    def mostrar_privilegios(self):
        print("Privilegios del admin:")
        for p in self.privilegios:
            print(f"- {p}")

admin1 = Admin("Carlos", "Lopez", ["puede_agregar_publicacion", "puede_eliminar_publicacion", "puede_banear_usuario"])
admin1.mostrar_privilegios()
