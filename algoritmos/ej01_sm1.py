def calcular_iva(precio, tasa=0.16):

    return precio * tasa

def main():

    precio_sin_iva=float(input("Ingresa el valor de la compra sin IVA:  "))
    iva = calcular_iva(precio_sin_iva)
    precio_con_iva = precio_sin_iva + iva

    print(f"Valor sin IVA: ${precio_sin_iva:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Valor con IVA : ${precio_con_iva:.2f}")

if __name__== "__main__":
    main()

