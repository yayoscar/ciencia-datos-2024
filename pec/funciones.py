import json
import os
DATOS_FILE = "aportes_ahorro.json"


def cargar_datos_ahorro():
    if not os.path.exists(DATOS_FILE):
        return {"meta_total": 0, "semanas_totales": 0, "aportes_registrados": []}

    try:
        with open(DATOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"meta_total": 0, "semanas_totales": 0, "aportes_registrados": []}


def guardar_datos_ahorro(datos):
    with open(DATOS_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def registrar_aporte(meta, semanas, aporte_actual):
    try:
        meta_num = float(meta)
        semanas_num = int(semanas)
        aporte_num = float(aporte_actual)
    except ValueError:
        return False

    datos = cargar_datos_ahorro()
    if meta_num > 0:
        datos["meta_total"] = meta_num
    if semanas_num > 0:
        datos["semanas_totales"] = semanas_num

    datos["aportes_registrados"].append(aporte_num)
    guardar_datos_ahorro(datos)
    return True


def calcular_progreso():
    datos = cargar_datos_ahorro()
    meta = datos.get("meta_total", 0)
    semanas_propuestas = datos.get("semanas_totales", 0)
    aportes = datos.get("aportes_registrados", [])

    ahorrado_total = sum(aportes)
    falta_ahorrar = max(0, meta - ahorrado_total)
    porcentaje_meta = (ahorrado_total / meta * 100) if meta > 0 else 0

    ritmo_mensaje = ""
    if meta > 0 and semanas_propuestas > 0:
        periodos_registrados = len(aportes)
        ahorro_esperado_por_periodo = meta / semanas_propuestas
        ahorro_proyectado_hasta_hoy = ahorro_esperado_por_periodo * periodos_registrados
        if ahorrado_total >= meta:
            ritmo_mensaje = "¡Felicidades! ¡Meta de ahorro alcanzada!"
        elif ahorrado_total >= ahorro_proyectado_hasta_hoy:
            ritmo_mensaje = "¡Vas a tiempo! Mantienes un excelente ritmo."
        else:
            ritmo_mensaje = f"Necesitas acelerar. Deberías llevar aprox. ${ahorro_proyectado_hasta_hoy:.2f}."
    elif meta > 0 and semanas_propuestas == 0:
        ritmo_mensaje = "Define un número de semanas para calcular el ritmo."
    else:
        ritmo_mensaje = "Define una meta y número de semanas para calcular el ritmo."

    return {
        "meta": meta,
        "ahorrado": ahorrado_total,
        "falta": falta_ahorrar,
        "porcentaje": porcentaje_meta,
        "ritmo_mensaje": ritmo_mensaje
    }


def borrar_todos_los_datos():
    if os.path.exists(DATOS_FILE):
        os.remove(DATOS_FILE)
        return True
    return False