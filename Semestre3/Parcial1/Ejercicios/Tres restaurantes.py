class Restaurante:
    def __init__(self,nombre, tipo):
        self.nombre_restaurante=nombre
        self.tipo_cocina=tipo
    def describir_restaurante(self):
        print(f"El nombre de este restaurante es {self.nombre_restaurante}"
              f" y su tipo de cocina es {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto")

restaurante1=Restaurante('Loncheria Chritopher','Venezolana')
restaurante2=Restaurante('Taqueria Asus','Mexicana')
restaurante3=Restaurante('La Olla de Diego','Americana')

restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()