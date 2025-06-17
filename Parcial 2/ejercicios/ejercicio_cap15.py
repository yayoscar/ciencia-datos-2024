# 1. Crea una lista de frutas con al menos 5 frutas
frutas = ["Manzana", "Banana", "Cereza", "Durazno", "Mango"]

# Imprime la segunda y la última fruta
print(frutas[1])  # Segunda fruta (índice 1)
print(frutas[-1])  # Última fruta (índice -1)

# 2. Crea una lista 'datos' con nombre, edad y si está registrado
datos = ["Carlos", 25, True]

# 3. Corrección de la línea
ciudades = ["Madrid", "París", "Roma", "Berlín"]  # Solo 4 ciudades

# Verifica que el índice exista antes de imprimir
if len(ciudades) > 5:
    print("Tu ciudad favorita es " + ciudades[5])
else:
    print("No hay suficientes ciudades en la lista")