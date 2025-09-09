class Restaurante:
    def __init__(self,nombre_restaurante,tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El nombre del restaurante es {self.nombre_restaurante}.")
        print(f"El tipo de cocina es {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto.")

mi_restaurante = Restaurante('Chefcito','gourmet')
print(f"El restaurante es {mi_restaurante.nombre_restaurante}.")
print(f"Su cocina es {mi_restaurante.tipo_cocina}.")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()