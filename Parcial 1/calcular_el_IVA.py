def calcular_iva (precio_sin_iva) :
    iva = precio_sin_iva * 0.16
    precio_con_iva = precio_sin_iva + iva
    return precio_sin_iva, precio_con_iva

# Entrada del usuario
precio = float (input("Introduce el valor de la compra: "))
sin_iva, con_iva = calcular_iva (precio)

# Resultados
print (f"Valor sin IVA: {sin_iva}")
print (f"Valor con IVA: {con_iva}")
