import csv
import os

ARCHIVO = "datos.csv"


def registrar_aporte(aporte):
    with open(ARCHIVO, "a", newline="") as archivo:
        xd = csv.writer(archivo)
        xd.writerow([aporte])


def leer_aportes():
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

