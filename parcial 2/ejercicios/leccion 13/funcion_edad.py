def obtener_edad(anio_nacimiento,anio_actual):
    años_actuales=anio_actual-anio_nacimiento
    respuesta=print(f"su edad es de {años_actuales}")
    return respuesta
anio_nacimiento=int(input("ingrese su año de nacimiento: "))
print(obtener_edad(anio_nacimiento,2025))


