class Restaurante:
    def __init__(self,nombre_restaurante,tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El nombre del restaurante es {self.nombre_restaurante}.")
        print(f"El tipo de cocina es {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto.")

comida = Restaurante('Chefcito','tradicional')
restaurante = Restaurante('El camino','gourmet')
restaurante2 = Restaurante('10 hermanos','fonda')

comida.describir_restaurante()
restaurante.describir_restaurante()
restaurante2.describir_restaurante()