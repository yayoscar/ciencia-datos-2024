def obtener_maximo():
    calificaciones = [9.6,9.2,9.7]
    maximo = max(calificaciones)
    minimo = min(calificaciones)
    return f"max: {maximo}, min {minimo}"


print(obtener_maximo())