import json
import os
#Profe necesitamos clases de usted enseñando json esta muy dificil ;/

archivo_datos = "Dato_meta_ahorro.json"

def cargar_datos_json ():
    if os.path.exists(archivo_datos):
        with open (archivo_datos, "r") as cargar_archivo:
            datos = json.load(cargar_archivo)
        return datos
    else:
        return {"meta": 0, "semanas": 0, "aportes": []}

def guardar_datos_en_archivo(metas,semanas,aportes):
    datos = cargar_datos_json()
    if not datos["aportes"]:
            datos["meta"] = metas
            datos["semanas"] = semanas
    datos["aportes"].append(aportes)
    with open(archivo_datos, "w") as archivo_write:
        json.dump(datos,archivo_write,indent=2)

def calcular_progreso():
    datos = cargar_datos_json()
    total_ahorrado = sum(datos["aportes"])
    meta = datos["meta"]
    restante = max(0, meta - total_ahorrado)
    porcentaje = min(100, (total_ahorrado / meta * 100) if meta > 0 else 0)
    if total_ahorrado >= meta:
        mensaje = f"Felicidades haz ahorrado ${total_ahorrado} ({porcentaje:.2f}% Felicidades cumpliste la meta"
    else:
        mensaje = f"llevas ${total_ahorrado} ahorrado ({porcentaje:.2f}$. Te faltan {restante}"

    return mensaje