def obtener_maximo():
    celsius = [14, 15.1, 12.3]
    maximo = max(celsius)
    return maximo  # <-- aquí está la clave

celsius = obtener_maximo()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)