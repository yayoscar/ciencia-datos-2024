def obtener_tasa(banco):
    tasas = {
        "Hey Banco": 0.10,  
        "NU": 0.085,
        "Finsus": 0.12
    }
    return tasas.get(banco, 0)

def calcular_monto_final(monto_inicial, ahorro_mensual, meses, tasa_anual):
    tasa_mensual = tasa_anual / 12
    monto_total = monto_inicial

    for _ in range(meses):
        monto_total += ahorro_mensual
        monto_total *= (1 + tasa_mensual)

    return round(monto_total, 2)
