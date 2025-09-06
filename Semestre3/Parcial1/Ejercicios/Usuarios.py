class Usuario:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre=nombre
        self.apellido=apellido
        self.edad = edad
        self.sexo=sexo
        self.intentos_inico_sesion=0
    def describir_usuario(self):
        print(f"El nombre del usuario es: {self.nombre} "
              f"El apellido del usuario es: {self.apellido} "
              f"La edad del usuario es: {self.edad} "
              f"El genero del usuario es: {self.sexo} ")
    def saludar_usuario(self):
        print(f"Saludos {self.nombre}, espero y este contento con nuestro servicio")
    def imcrementar_intentos_inicio_sesion(self):
        self.intentos_inico_sesion+=1
    def reiniciar_intentos_inicio_sesion(self):
        self.intentos_inico_sesion=0

usuario1=Usuario('Wilian','Barzon',16,'Hombre')
usuario2=Usuario('Diego','Tuz',16,'Hombre')
usuario3=Usuario('Christopher','Tapia',16,'Hombre')
usuario4=Usuario('Andres','Mendoza',20,'Hombre')

usuario1.describir_usuario()
usuario1.saludar_usuario()
print()
usuario2.describir_usuario()
usuario2.saludar_usuario()
print()
usuario3.describir_usuario()
usuario3.saludar_usuario()
print()
usuario4.describir_usuario()
usuario4.saludar_usuario()


usuario1.imcrementar_intentos_inicio_sesion()
usuario1.imcrementar_intentos_inicio_sesion()
usuario1.imcrementar_intentos_inicio_sesion()
usuario1.imcrementar_intentos_inicio_sesion()
print(f"Intentos actuales de inicio de sesion: {usuario1.intentos_inico_sesion}")

usuario1.reiniciar_intentos_inicio_sesion()
print(f"Intentos de inicio de sesion despues de reiniciar: {usuario1.intentos_inico_sesion}")