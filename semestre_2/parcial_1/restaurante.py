class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        self.numero_servidos = 0
    def describir_restaurante(self):
        return f"{self.nombre_restaurante} es un restaurante de comida {self.tipo_cocina}"
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto!")
    def leer_numeroservidos(self):
        print(f"{self.nombre_restaurante} ha atendido a {self.numero_servidos} clientes")
    def establecer_numero_servidos(self, servidos):
        self.numero_servidos = servidos
    def incrementer_numero_servidos(self, servidos):
        self.numero_servidos += servidos
class PuestoHelados(Restaurante):
    def __init__(self, nombre, tipo, sabores):
        super().__init__(nombre, tipo)
        self.sabores = sabores
    def mostrar_sabores(self):
        print(f"El puesto de helados {self.nombre_restaurante} tiene los sabores:")
        for n,sabor in enumerate(self.sabores):
            print(f"{n+1}.-{sabor}")

    def describir_restaurante(self):
        return f"Hola{Restaurante.describir_restaurante(self)}"
