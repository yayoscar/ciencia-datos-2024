def obtener_maximo():
    celsius = [14, 15.1, 12.3]
    return max(celsius)

max_celsius = obtener_maximo()

fahrenheit = max_celsius * 1.8 + 32

print(f"El valor máximo en Celsius es: {max_celsius}")
print(f"Convertido a Fahrenheit: {fahrenheit:.1f}")

