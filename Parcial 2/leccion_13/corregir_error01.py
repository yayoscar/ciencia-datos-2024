def calcular_tiempo(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

tiempo = calcular_tiempo(100)
print(tiempo)