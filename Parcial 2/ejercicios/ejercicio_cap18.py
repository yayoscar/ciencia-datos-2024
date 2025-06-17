# Lista de compras
compras = ["Leche", "Pan", "Huevos", "Pagar renta", "Frutas"]

# 1. Elimina el primer elemento
del compras[0]
print(compras)

# 2. Elimina "Pagar renta" usando .remove()
compras.remove("Pagar renta")
print(compras)

# 3. Intenta eliminar un elemento inexistente y observa el error
try:
    compras.remove("Chocolate")  # No está en la lista
except ValueError as e:
    print(f"Error: {e}")