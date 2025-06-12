import csv

def guardar_datos(monto,categoria,fecha):
    with open("datos.csv", mode="a", newline="", ) as archivo:
        dat_guar = csv.writer(archivo)
        dat_guar.writerows([monto,categoria,fecha])


def mostrar_gastos():
    resumen = []
    with open("datos.csv", "r") as d:
        contenido = csv.DictReader(d)
        for fila in contenido:
            linea = f"{fila['MONTO']} - {fila['CATEGORIA']} - {fila['FECHA']}"
            resumen.append(linea)
        return resumen

