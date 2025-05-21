def calcular_iva():
    print("calculadora de IVA")

    precio_compra= float(input("ingresa el precio de compra en pesos:"))
    comision_porcentaje= float(input("ingresa el porcentaje de comision(16%): "))

    comision = precio_compra*(comision_porcentaje/100)
    valor_final = precio_compra+comision

    print("\n === resultado ===")
    print(f"monto de compra: ${precio_compra:,.2f}pesos")
    print(f"comision estimada: ${comision:,.2f}pesos")
    print(f"valor despues de la comision: ${valor_final:,.2f}pesos")

calcular_iva()
