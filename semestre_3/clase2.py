class Usuario:
    def __init__(self,nombre,apellido,sexo,edad,correo,contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.correo = correo
        self.contrasena = contrasena
    def describir_usuario(self):
        print(f" nombre: {self.nombre}")
        print(f" apellido: {self.apellido}")
        print(f" edad: {self.edad}")
        print(f" sexo: {self.sexo}")
        print(f" correo: {self.correo}")
        print(f" contraseña: {self.contrasena}")
    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}")

usuario1 = Usuario("Yulitza",'Alcocer','mujer','15','yulitza@gmail.com','YULITZA2025')
usuario2= Usuario('Victoria','Balam','mujer','15','victoria@gmail.com','VICTORIA2025')
usuario3 = Usuario('Pacho','Ucan','hombre','15','pacho@gmail.com','PACHO2025')

usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario()
usuario3.describir_usuario()
usuario3.saludar_usuario()