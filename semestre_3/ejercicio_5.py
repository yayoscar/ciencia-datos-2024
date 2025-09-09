class Usuario:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.intentos_inicio_sesion = 0

    def describir_usuario(self):
        print(" Información del Usuario")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Género: {self.genero}")

    def saludar_usuario(self):
        print(f"¡Bienvenido {self.nombre}! Espero que hoy sea un gran día")

    def incrementar_intentos_sesion(self):
        self.intentos_inicio_sesion += 1

    def reiniciar_intentos_inicio_sesion(self):
        self.intentos_inicio_sesion = 0


# Creación de la instancia con otros valores
usuario1 = Usuario("Itzel", "Hernández", 18, "femenino")

# Uso de los métodos
usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario1.incrementar_intentos_sesion()
usuario1.incrementar_intentos_sesion()

print(f"Intentos de inicio de sesión de {usuario1.nombre}: {usuario1.intentos_inicio_sesion}")

usuario1.reiniciar_intentos_inicio_sesion()
print(f"Intentos de inicio de sesión de {usuario1.nombre} después de reiniciar: {usuario1.intentos_inicio_sesion}")
