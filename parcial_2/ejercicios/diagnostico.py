nombre = "Daniela"
saludo = "¡Hola, " + nombre + "!"
print(saludo)

precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio_unitario * cantidad
print(f"El total es: {total}")

temperatura = int(input("Ingrese la temperatura"))
if temperatura <15:
    print("Hace frío")
elif 15 <= temperatura <25:
    print("Clima agradable")
else:
    print("Hace fresco")

compras = ["leche", "huevos", "pan", "queso"]
compras.append("jamon")
compras[1] = "yogurt"
del compras[0]
print(compras)