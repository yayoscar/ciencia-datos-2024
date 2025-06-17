def calcular_tiempo(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
print(calcular_tiempo(100))