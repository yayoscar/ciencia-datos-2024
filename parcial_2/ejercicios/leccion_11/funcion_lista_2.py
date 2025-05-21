def obtener_maximo():
    calificaciones = [9.6,9.2,9.7]
    maximo_local = max(calificaciones)
    minimo = min(calificaciones)
    return f"Max: {maximo_local}, min: {minimo}"


print(obtener_maximo())