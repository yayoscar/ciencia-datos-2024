def calcular_ahorro(precio, veces, meses):
    semanas_por_mes = 4.3
    total_semanas = meses * semanas_por_mes
    gasto_total = precio * veces * total_semanas
    return gasto_total