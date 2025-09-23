class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
    def describir_restaurante(self):
        print(f"{self.nombre_restaurante} es un restaurante {self.tipo_cocina}")
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto!")
sushi = Restaurante("Mi suchi", "Japonés")
taquito = Restaurante("Taquito", "Mexicano")
thai = Restaurante("Boonchoi", "Tailandés")
sushi.describir_restaurante()
taquito.describir_restaurante()
thai.describir_restaurante()