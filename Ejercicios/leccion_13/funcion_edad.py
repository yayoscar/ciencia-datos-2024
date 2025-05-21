from datetime import datetime

def obtener_edad(anio_nacimiento, anio_actual=datetime.now().year):
    return anio_actual - anio_nacimiento

edad = obtener_edad(2000)
print(f"La edad calculada es: {edad}")
