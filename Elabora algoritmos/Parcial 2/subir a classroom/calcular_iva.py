def calcular_iva(monto, tasa=0.16):
    iva = monto * tasa
    total = monto + iva
    return iva, total

try:
    monto_sin_iva = float(input("Ingresa el monto de la compra sin IVA: $"))
    iva, total_con_iva = calcular_iva(monto_sin_iva)

    print("\n--- Detalle de la compra ---")
    print("Monto sin IVA: $", round(monto_sin_iva, 2))
    print("IVA (16%):     $", round(iva, 2))
    print("Total con IVA: $", round(total_con_iva, 2))
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")
