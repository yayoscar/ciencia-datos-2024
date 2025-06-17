import csv
import os

ARCHIVO = "datos.csv"

def registrar_aporte(aporte):
    with open(ARCHIVO, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([aporte])

def leer_aportes():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as archivo:
        reader = csv.reader(archivo)
        return [float(fila[0]) for fila in reader if fila]

def calcular_progreso(meta, semanas):
    aportes = leer_aportes()
    total_ahorrado = sum(aportes)
    faltante = max(0, meta - total_ahorrado)
    semanas_transcurridas = len(aportes)

    mensaje = f"""Has ahorrado: ${total_ahorrado:.2f} de ${meta:.2f}.
     Semanas transcurridas: {semanas_transcurridas} de {semanas}"""

    if total_ahorrado >= meta:
        mensaje += "Meta alcanzada, eres un crack, idolo, genio, master, mastodonte "
    elif semanas_transcurridas < semanas:
        mensaje += f" Te falta ${faltante:.2f} pesos, sigue asi crack"
    else:
        mensaje += f"Meta no alcanzado que paso crack te falto ${faltante:.2f}."

    return mensaje

