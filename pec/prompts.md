que error tiene mi codigo? import FreeSimpleGUI as sg
from funciones import registrar_aporte, calcular_progreso

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Salir")]
]

window = sg.Window("Programa de Ahorro", layout)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Registrar aporte":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            aporte = float(values["APORTE"])
            registrar_aporte(aporte)
            sg.popup("Aporte registrado con éxito.")
        except ValueError:
            sg.popup_error("Por favor ingresa solo numeros.")
    elif event == "Ver progreso":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            progreso_texto = calcular_progreso(meta, semanas)
            sg.popup("esto llevas de la meta", progreso_texto)
        except ValueError:
            sg.popup_error("Por favor completa todos los campos correctamente.")

window.close()

ChatGPT Plus
Tu código está muy bien estructurado y casi correcto, pero el error principal está en esta línea:

python
Copiar
Editar
import FreeSimpleGUI as sg
❌ Error:
FreeSimpleGUI no existe como módulo en Python.

✅ Corrección:
Debes usar:

python
Copiar
Editar
import PySimpleGUI as sg
✅ Otros detalles menores (opcional, pero recomendados):
Mensaje más claro en sg.popup:

python
Copiar
Editar
sg.popup("✅ Aporte registrado con éxito.")
Encabezado más claro para el progreso:

python
Copiar
Editar
sg.popup("📊 Progreso de ahorro", progreso_texto)
📌 Código corregido:
python
Copiar
Editar
import PySimpleGUI as sg
from funciones import registrar_aporte, calcular_progreso

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso"), sg.Button("Salir")]
]

window = sg.Window("Programa de Ahorro", layout)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Registrar aporte":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            aporte = float(values["APORTE"])
            registrar_aporte(aporte)
            sg.popup("✅ Aporte registrado con éxito.")
        except ValueError:
            sg.popup_error("❌ Por favor ingresa solo números.")
    
    elif event == "Ver progreso":
        try:
            meta = float(values["META"])
            semanas = int(values["SEMANAS"])
            progreso_texto = calcular_progreso(meta, semanas)
            sg.popup("📊 Progreso de ahorro", progreso_texto)
        except ValueError:
            sg.popup_error("❌ Por favor completa todos los campos correctamente.")

window.close()
¿Quieres que revise también tu archivo funciones.py por si hay errores allí?

si, def leer_aportes():
    if not os.path.exists(ARCHIVO):
        return ()

    with open(ARCHIVO, "r") as archivo:
        nose = csv.reader(archivo)
        return (float(fila[0]) for fila in nose if fila)


def calcular_progreso(meta, semanas):
    aportes = leer_aportes()
    total_ahorrado = sum(aportes)
    faltante = max(0, meta - total_ahorrado)

    mensaje = f"Has ahorrado ${total_ahorrado:.2f}."
    if total_ahorrado >= meta:
        mensaje = "ERES UN CRACK LO LOGRASTE, META CUMPLITDA"
    else:
        mensaje = f" Te faltan ${faltante:.2f}."
        if len(aportes) < semanas:
            mensaje = f" Aún te quedan {semanas - len(aportes)} semana crack para completar tu meta."
        else:
            mensaje = "que paso ahi crack has terminado tus semanas y no alcanzaste la meta :("

    return mensaje

ChatGPT Plus
Gracias por compartir tu código. Te comento los errores y mejoras necesarias en tu archivo funciones.py:

❌ ERRORES
1. Tipo de retorno incorrecto en leer_aportes()
Estás retornando una tupla generadora:

python
Copiar
Editar
return (float(fila[0]) for fila in nose if fila)
Eso funciona para sum(), pero no para len(), lo cual lanza:

python
Copiar
Editar
TypeError: object of type 'generator' has no len()
✅ SOLUCIÓN:
Convierte el generador a una lista:

python
Copiar
Editar
return [float(fila[0]) for fila in nose if fila]
2. Retorno incorrecto si no existe el archivo
Actualmente:

python
Copiar
Editar
return ()
Es una tupla vacía. Mejor usar una lista vacía, por consistencia con el retorno corregido.

✅ SOLUCIÓN:
python
Copiar
Editar
return []
3. Sobrescribes mensaje varias veces
En esta parte:

python
Copiar
Editar
mensaje = f"Has ahorrado ${total_ahorrado:.2f}."
if total_ahorrado >= meta:
    mensaje = "ERES UN CRACK..."
else:
    mensaje = f" Te faltan ${faltante:.2f}."
    ...
Estás reemplazando el mensaje anterior en vez de acumularlo.

✅ SOLUCIÓN:
Usa += para ir agregando contenido al mensaje.

4. No has definido ARCHIVO
Asegúrate de definir al inicio del archivo:

python
Copiar
Editar
ARCHIVO = "datos.csv"
✅ VERSIÓN CORREGIDA DE funciones.py
python
Copiar
Editar
import csv
import os

ARCHIVO = "datos.csv"

def leer_aportes():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as archivo:
        reader = csv.reader(archivo)
        return [float(fila[0]) for fila in reader if fila]

def registrar_aporte(aporte):
    with open(ARCHIVO, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([aporte])

def calcular_progreso(meta, semanas):
    aportes = leer_aportes()
    total_ahorrado = sum(aportes)
    faltante = max(0, meta - total_ahorrado)

    mensaje = f"Has ahorrado ${total_ahorrado:.2f}.\n"

    if total_ahorrado >= meta:
        mensaje += "🎉 ERES UN CRACK, ¡LO LOGRASTE! META CUMPLIDA 💪"
    else:
        mensaje += f"Te faltan ${faltante:.2f}.\n"
        if len(aportes) < semanas:
            mensaje += f"Aún te quedan {semanas - len(aportes)} semana(s) para completar tu meta. 🔄"
        else:
            mensaje += "😓 Ya pasaron las semanas y no alcanzaste la meta. ¡No te rindas!"

    return mensaje