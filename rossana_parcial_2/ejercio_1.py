def calcular_iva(precio_sin_iva):
    iva = precio_sin_iva * 0.16
    precio_con_iva = precio_sin_iva + iva
    return iva, precio_con_iva

precio_sin_iva = float(input("ingresa el valor de la compra sin IVA:"))
iva, precio_con_iva = calcular_iva(precio_sin_iva)

print(f"valor de la compra sin iva: ${precio_con_iva:.2f}")
print(f"iva (16%): ${iva:.2f}")
print(f"valor de la compra con iva: ${precio_con_iva:.2f}")