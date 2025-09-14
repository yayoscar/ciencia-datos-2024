class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Nombre: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

restaurante = Restaurante("La Buena Mesa", "Italiana")
print(restaurante.nombre_restaurante)
print(restaurante.tipo_cocina)
restaurante.describir_restaurante()
restaurante.abrir_restaurante()
