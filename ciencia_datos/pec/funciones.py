import csv
from collections import defaultdict
from datetime import datetime

def guardar_gasto(monto, categoria, fecha=""):
    if not fecha:
        fecha = datetime.today().strftime("%Y-%m-%d")
    with open("gastos.csv", mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([fecha, categoria, monto])

def generar_resumen():
    resumen = defaultdict(float)
    total = 0.0
    try:
        with open("gastos.csv", mode="r") as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                if len(fila) == 3:
                    _, categoria, monto = fila
                    try:
                        monto = float(monto)
                        resumen[categoria] += monto
                        total += monto
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return resumen, total