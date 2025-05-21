def obtener_maximo():
    calificaciones = [9.6,9.2,9.7]
    maximo_local = max(calificaciones)
    minimo_local = min(calificaciones)
    return f"Max: {maximo_local}, Min: {minimo_local}"

print(obtener_maximo())