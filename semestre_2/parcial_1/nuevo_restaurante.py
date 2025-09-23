from restaurante import Restaurante, PuestoHelados

sushi = Restaurante("Mi suchi", "Japonesa")
print(sushi.nombre_restaurante)
print(sushi.tipo_cocina)
sushi.describir_restaurante()
sushi.abrir_restaurante()
sushi.leer_numeroservidos()
sushi.numero_servidos = 3
sushi.leer_numeroservidos()
sushi.establecer_numero_servidos(9)
sushi.leer_numeroservidos()
sushi.incrementer_numero_servidos(3)
sushi.leer_numeroservidos()

sabores = ['chocolate', 'vainilla', 'napolitano']
heladito = PuestoHelados("La Michoacana", "Helados", sabores)
heladito.mostrar_sabores()
print(heladito.describir_restaurante())