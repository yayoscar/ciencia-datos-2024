import json
import os

def cargar_datos(nombre_archivo="datos.json"):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            return json.load(f)
    else:
        return {"meta": 0, "semanas": 0, "aportes": []}

def guardar_datos(meta, semanas, aportes, nombre_archivo="datos.json"):
    datos = {"meta": meta, "semanas": semanas, "aportes": aportes}
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

def calcular_progreso(meta, aportes):
    total_ahorrado = sum(aportes)
    porcentaje = (total_ahorrado / meta) * 100 if meta > 0 else 0
    falta = meta - total_ahorrado
    return total_ahorrado, porcentaje, falta