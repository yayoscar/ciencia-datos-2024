from ej4_clientes import RestauranteConClientes

class PuestoHelados(RestauranteConClientes):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")

heladeria = PuestoHelados("Helados Deliciosos", "Postres", ["Vainilla", "Chocolate", "Fresa"])
heladeria.mostrar_sabores()
