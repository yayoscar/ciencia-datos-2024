class Usuario:
    def __init__(self, nombre, apellido, edad=None, email=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        if self.edad:
            print(f"Edad: {self.edad}")
        if self.email:
            print(f"Email: {self.email}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre}, ¡bienvenido/a!")

user1 = Usuario("Daniela", "Chin", 20, "daniela@mail.com")
user2 = Usuario("Zael", "Gomez", 21, "zael@mail.com")

user1.describir_usuario()
user1.saludar_usuario()
user2.describir_usuario()
user2.saludar_usuario()
