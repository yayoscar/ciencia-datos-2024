class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        self.numeros_servidos = 1

    def describir_restaurante(self):
        print(f"El nombre de este restaurante es {self.nombre_restaurante}"
              f" y su tipo de cocina es {self.tipo_cocina}")

    def restaurante_abierto(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto")

    def mostrar_numero_servidos(self):
        print(f"El numero de clientes atendidos es: {self.numeros_servidos}")

    def establecer_numero_servidos(self, numero):
        if numero >= 0:
            self.numeros_servidos = numero
        else:
            print("El numero de clientes no puede ser negativo")

    def incrementar_numero_servidos(self, numero):
        if numero > 0:
            self.numeros_servidos += numero
        else:
            print("Se debe incrementar")


Antojitos = Restaurante('Nose', 'Italiana')

print(f"El restaurannte se llama {Antojitos.nombre_restaurante}")
print(f"El tipo de cocina es {Antojitos.tipo_cocina}")
Antojitos.describir_restaurante()
Antojitos.restaurante_abierto()

Antojitos.mostrar_numero_servidos()
Antojitos.numeros_servidos = 40
Antojitos.mostrar_numero_servidos()
Antojitos.establecer_numero_servidos(45)
Antojitos.mostrar_numero_servidos()