def obtener_maximo():
    calificaciones = [9.6, 9.2, 9.7]
    maximo = max(calificaciones)
    minimo = min(calificaciones)
    return f"Max: {maximo}, Min: {minimo}"


print(obtener_maximo())