from ej1_restaurante import Restaurante

class RestauranteConClientes(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.numero_servidos = 0

    def establecer_numero_servidos(self, numero):
        self.numero_servidos = numero

    def incrementar_numero_servidos(self, incremento):
        self.numero_servidos += incremento

restaurante2 = RestauranteConClientes("La Comida Feliz", "Internacional")
print(restaurante2.numero_servidos)
restaurante2.numero_servidos = 5
print(restaurante2.numero_servidos)
restaurante2.establecer_numero_servidos(20)
print(restaurante2.numero_servidos)
restaurante2.incrementar_numero_servidos(10)
print(restaurante2.numero_servidos)
