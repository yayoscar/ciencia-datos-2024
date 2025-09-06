class usuario:
    def __init__(self,nombre,apellido,sexo,edad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.apellido=apellido
        return
    def describir_usuario(self):
        print(f"El usuario {self.nombre},{self.apellido}, tiene {self.edad} años,{self.sexo}")
    def saludar_usuario (self):
        print(f"Hola{self.nombre},gracias por entrar")
        juan=usuario("juan","Martinez","15","hombre")
        juan.describir_usuario()
        juan.saludar_usuario()


