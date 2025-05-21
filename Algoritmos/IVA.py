def calcular_iva(precio_sin_iva):
    iva = precio_sin_iva * 0.16
    precio_con_iva = precio_sin_iva + iva
    return precio_con_iva

precio_sin_iva = float(input("Ingresa el valor de la compra sin IVA: "))

precio_con_iva = calcular_iva(precio_sin_iva)
print(f"Valor sin IVA: ${precio_sin_iva:.2f}")
print(f"Valor con IVA (16%): ${precio_con_iva:.2f}")