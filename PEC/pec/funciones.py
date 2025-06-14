import csv
from collections import defaultdict
from datetime import datetime
import os

ARCHIVO = "gastos.csv"

def guardar_gasto(monto, categoria, fecha=None):
    if fecha:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            fecha = None

    with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([monto, categoria, fecha or ""])

def resumen():
    resumen = defaultdict(float)
    total = 0.0

    if not os.path.exists(ARCHIVO):
        return resumen, total

    with open(ARCHIVO, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                monto = float(row[0])
                categoria = row[1]
                resumen[categoria] += monto
                total += monto
            except (IndexError, ValueError):
                continue

    return resumen, total