from pec.main import monto_inicial

tasas = {
    "Hey Banco": 0.10,
    "NU": 0.135,
    "Finsus": 0.145
}

def obtener_tasa(banco):
    return tasas.get(banco, 0)

def calcular_ahorro(cantidad_inicial, mensual, meses, tasa_anual):
    tasa_mensual = tasa_anual / 12
    total = cantidad_inicial
    for _ in range(meses):
        total = (total + mensual) * (1 + tasa_mensual)
    return round(total, 2)

def guardar_resultado_csv(nombre_archivo, cantidad_incial, mensual, meses, banco, total):
    import csv
    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["cantidad incial", "Ahorro Mensual", "Meses", "Banco", "Total Final"])
        writer.writerow([cantidad_incial, mensual, meses, banco, total])