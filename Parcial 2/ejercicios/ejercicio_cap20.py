# 1. Crea una tupla con 4 equipos de fútbol mexicano
equipos = ("América", "Chivas", "Cruz Azul", "Pumas")

# 2. Imprime el tercer equipo
print("El tercer equipo es:", equipos[2])

# 3. Intenta modificar un valor (observa el error)
try:
    equipos[0] = "Tigres"  # Intento de modificar un valor en la tupla
except TypeError as e:
    print(f"Error: {e}")

# Redefine la tupla correctamente
equipos = ("América", "Chivas", "Cruz Azul", "Pumas", "Tigres")  # Redefinida con "Tigres"
print("Tupla redefinida:", equipos)