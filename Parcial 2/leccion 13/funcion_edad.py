def obtener_edad(anio_nacimiento, anio_actual = 2025):
    edad = anio_actual-anio_nacimiento
    return edad
print(obtener_edad(2009))