class Usuario:
    def _init_(self,nombre,apellido,edad,sexo):
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
        print(f"Saludos {self.nombre}")
    def imcrementar_intentos_inicio_sesion(self):
        self.intentos_inico_sesion+=1
    def reiniciar_intentos_inicio_sesion(self):
        self.intentos_inico_sesion=0

usuario1=Usuario('Kamila','Martinez',16,'Mujer')
usuario3=Usuario('Cricri','Delgado',16,'Mujer')
usuario4=Usuario('Eusebio','Pool',16,'Hombre')
usuario2=Usuario('Ian','Marin',16,'Hombre')

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
print(f"Intentos en la sesion: {usuario1.intentos_inico_sesion}")

usuario1.reiniciar_intentos_inicio_sesion()
print(f"Se reinicia en {usuario1.intentos_inico_sesion} intentos")