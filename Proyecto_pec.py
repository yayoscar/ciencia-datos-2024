import FreeSimpleGUI as sg
import json
import os

def registrar_aporte(meta, semanas, aporte_actual, aportes_anteriores):
    """Registra un nuevo aporte en un archivo JSON."""

    try:
        aporte_actual = float(aporte_actual) # Asegurar que el aporte es un número
        aportes_anteriores.append(aporte_actual)

        data = {
            "meta": meta,
            "semanas": semanas,
            "aportes": aportes_anteriores
        }

        with open("ahorros.json", "w") as f:
            json.dump(data, f, indent=4) # Formato legible
        return True

    except ValueError:
        sg.popup_error("Por favor, ingresa un aporte numérico.")
        return False
    except Exception as e:
        sg.popup_error(f"Error al registrar el aporte: {e}")
        return False


def mostrar_progreso(meta, semanas, aportes):

    total_ahorrado = sum(aportes)
    porcentaje = (total_ahorrado / meta) * 100 if meta > 0 else 0

    mensaje = f"""
    Has ahorrado ${total_ahorrado:.2f} ({porcentaje:.2f}%)
    """
    if total_ahorrado >= meta:
        mensaje += "¡Meta cumplida!"
    else:
        faltante = meta - total_ahorrado
        mensaje += f"Faltan ${faltante:.2f} para alcanzar la meta."

    sg.popup(mensaje)

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
]

window = sg.Window("Reto de Ahorro", layout)

if os.path.exists("ahorros.json"):
    with open("ahorros.json", "r") as f:
        data = json.load(f)
        meta_actual = data["meta"]
        semanas_actual = data["semanas"]
        aportes_actuales = data["aportes"]
else:
    meta_actual = 0
    semanas_actual = 0
    aportes_actuales = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Registrar aporte":
        if not all(values.values()): # Verifica que todos los campos esten llenos
            sg.popup_error("Por favor, completa todos los campos.")
            continue
        if registrar_aporte(float(values["META"]), int(values["SEMANAS"]), values["APORTE"], aportes_actuales):
            aportes_actuales = []
            with open("ahorros.json", "r") as f:
                data = json.load(f)
                aportes_actuales = data["aportes"]

    if event == "Ver progreso":
        if not aportes_actuales:
            sg.popup_error("No hay aportes registrados aún.")
            continue
        mostrar_progreso(float(values["META"]), int(values["SEMANAS"]), aportes_actuales)

window.close()