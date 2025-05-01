tareas = ["Pagar luz", "Ir al banco", "Llamar al doctor"]
pendientes = ["Sacar al perro", "Ver Hamilton"]
print(tareas, pendientes)
terminadas = []
terminadas.append(tareas.pop(0))
print(terminadas)
terminadas.append(pendientes.pop())
print(terminadas)