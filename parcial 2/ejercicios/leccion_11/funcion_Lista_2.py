def obtener_maximo():
    calificaciones = [9.6, 9.2, 9.7]
    maximo = max(calificaciones)
    return maximo
def obtener_minimo():
    calificaciones = [9.6, 9.2, 9.7]
    minimo = min(calificaciones)
    return minimo


print(f"Max:", obtener_maximo(), f"Min: ", obtener_minimo())