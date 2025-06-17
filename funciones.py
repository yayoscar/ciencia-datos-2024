import json
import os
import FreeSimpleGUI as sg


ARCHIVO = 'datos.json'

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"meta": 0, "semanas": 0, "aportes": []}

def guardar_datos(datos):
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def registrar_aporte(meta, semanas, aporte):
    datos = cargar_datos()

    if datos["meta"] == 0 or datos["semanas"] == 0:
        datos["meta"] = meta
        datos["semanas"] = semanas

    if len(datos["aportes"]) >= datos["semanas"]:
        sg.popup("Ya registraste todas las semanas.")
        return

    aporte_esperado = datos["meta"] / datos["semanas"]
    comentario = "Bien esta semana" if aporte == aporte_esperado else f"Me faltó ${aporte_esperado - aporte:.2f}"
    semana_num = len(datos["aportes"]) + 1

    nuevo_aporte = {
        "Semana": semana_num,
        "Aporte Real": aporte,
        "Aporte Esperado": round(aporte_esperado, 2),
        "Comentario": comentario
    }

    datos["aportes"].append(nuevo_aporte)
    guardar_datos(datos)

    sg.popup(f"Semana {semana_num} registrada correctamente.")

def mostrar_progreso():
    datos = cargar_datos()
    if not datos["aportes"]:
        sg.popup("Aún no hay datos registrados.")
        return

    texto = f"Meta total: ${datos['meta']}\n"
    texto += f"Número de semanas: {datos['semanas']}\n\n"

    for entrada in datos["aportes"]:
        texto += (
            f"Semana {entrada['Semana']}:\n"
            f"- Aporte Real: ${entrada['Aporte Real']}\n"
            f"- Aporte Esperado: ${entrada['Aporte Esperado']}\n"
            f"- Comentario: {entrada['Comentario']}\n\n"
        )

    sg.popup_scrolled("Progreso Actual", texto, size=(50, 20))

def reiniciar_progreso():
    confirmacion = sg.popup_yes_no("¿Estás seguro de que quieres reiniciar todo el progreso?")
    if confirmacion == "Yes":
        if os.path.exists(ARCHIVO):
            os.remove(ARCHIVO)
            sg.popup("Progreso reiniciado. Puedes comenzar desde cero.")


        else:
            sg.popup("El archivo ya estaba vacío.")
