class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.intentos_inicio_sesion = 0
    def describir_usuario(self):
        print(f"""Nombre: {self.nombre}
Apellido: {self.apellido}
Correo: {self.correo}
Contraseña: {self.contraseña}""")
    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}!")
    def incrementar_intentos_inicio_sesion(self):
        self.intentos_inicio_sesion += 1
    def reiniciar_intentos_inicio_sesion(self):
        self.intentos_inicio_sesion = 0

