import csv
tasass = {
    "NU": 0.135,
    "Finsus": 0.15,
    "Hey Banco": 0.12
}
def calcular_ahorro(inicial, mensual, meses, tasa_anual):
    tasa_mensual = tasa_anual / 12
    monto = inicial
    for _ in range(meses):
        monto = (monto + mensual) * (1 + tasa_mensual)
    return monto

def guardar_csv(fecha, banco, inicial, mensual, meses, tasa, total, archivo="simulacion_ahorro.csv"):
    with open(archivo, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([fecha, banco, inicial, mensual, meses, f"{tasa*100:.2f}%", f"{total:.2f}"])