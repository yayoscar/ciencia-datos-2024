def obtener_edad(anio_actual=2025):
    diferencia = anio_actual - anio_nacimiento
    return diferencia
anio_nacimiento = int(input("ingrese el anio en el que nacio  "))
print(f"su edad aproximada es de {obtener_edad()} anios")
