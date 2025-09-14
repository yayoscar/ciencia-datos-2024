class UsuarioConIntentos:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_inicio_sesion = 0

    def incrementar_intentos_inicio_sesion(self):
        self.intentos_inicio_sesion += 1

    def reiniciar_intentos_inicio_sesion(self):
        self.intentos_inicio_sesion = 0

user = UsuarioConIntentos("Ana", "Perez")
user.incrementar_intentos_inicio_sesion()
user.incrementar_intentos_inicio_sesion()
print(user.intentos_inicio_sesion)
user.reiniciar_intentos_inicio_sesion()
print(user.intentos_inicio_sesion)
