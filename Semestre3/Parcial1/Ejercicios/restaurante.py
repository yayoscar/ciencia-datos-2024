class Restaurante:
    def __init__(self,nombre, tipo):
        self.nombre_restaurante=nombre
        self.tipo_cocina=tipo
        self.numeros_servidos=0
    def describir_restaurante(self):
        print(f"El nombre de este restaurante es {self.nombre_restaurante}"
              f" y su tipo de cocina es {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto")
    def mostrar_numero_servidos(self):
        print(f"El numero de clientes atendidos es: {self.numeros_servidos}")
    def establecer_numero_servidos(self,numero):
        if numero >= 0:
            self.numeros_servidos=numero
        else:
            print("El numero de clientes no puede ser negativo")
    def incrementar_numero_servidos(self,numero):
        if numero > 0:
            self.numeros_servidos +=numero
        else:
            print("Se debe incrementar")
    
Cocina_Guille=Restaurante('Cocina Guille', 'Mexicana')

print(f"El restaurannte se llama {Cocina_Guille.nombre_restaurante}")
print(f"El tipo de cocina es {Cocina_Guille.tipo_cocina}")
Cocina_Guille.describir_restaurante()
Cocina_Guille.abrir_restaurante()

Cocina_Guille.mostrar_numero_servidos()
Cocina_Guille.numeros_servidos=10
Cocina_Guille.mostrar_numero_servidos()
Cocina_Guille.establecer_numero_servidos(25)
Cocina_Guille.mostrar_numero_servidos()
Cocina_Guille.incrementar_numero_servidos(15)
Cocina_Guille.mostrar_numero_servidos()