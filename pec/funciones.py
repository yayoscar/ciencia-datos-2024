import csv
import os
from collections import defaultdict
from datetime import date

ARCHIVO = "datos.csv"

def guardar_datos(monto,categoria,fecha = ""):
    if not fecha:
        fecha = date.today().isoformat()
    with open("datos.csv", mode="a", newline="", encoding="utf-8" ) as archivo:
        campos = ["MONTO", "CATEGORIA", "FECHA"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            writer.writeheader()
        writer.writerow({"MONTO": monto, "CATEGORIA": categoria, "FECHA": fecha})


def mostrar_gastos(detalle=False):
    if not os.path.exists(ARCHIVO):
        return "Aún no hay registros."
    todos = defaultdict(float)
    resumen = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        contenido = csv.DictReader(archivo)
        for fila in contenido:
            resumen.append(f"{fila['FECHA']} | {fila['CATEGORIA']} | ${fila['MONTO']}")
            try:
                todos[fila["CATEGORIA"]] += float(fila["MONTO"])
            except ValueError:
                pass
        if detalle:
            return "\n".join(resumen) or "Aún no hay registros."

        if not todos:
            return "Aún no hay registros."

        lineas = [f"{cat}: ${todos[cat]:.2f}" for cat in sorted(todos)]
        return "\n".join(lineas)
