# Lista de pendientes
pendientes = ["Hacer tarea", "Lavar platos", "Comprar comida"]

# 1. Usa .pop() para guardar el primer pendiente en una variable
primer_pendiente = pendientes.pop(0)
print("Primer pendiente extraído:", primer_pendiente)

# 2. Agrégalo a una lista 'terminadas'
terminadas = []
terminadas.append(primer_pendiente)
print("Lista de tareas terminadas:", terminadas)

# 3. Usa .pop() sin argumento para sacar el último elemento de otra lista
ultimo_pendiente = pendientes.pop()
print("Último pendiente extraído:", ultimo_pendiente)
print("Lista de pendientes actualizada:", pendientes)