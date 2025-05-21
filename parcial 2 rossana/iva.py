def calcular_iva():
    precio=float(input("ingrese el precio de compra"))
    iva= precio*0.16
    total=precio+iva
    print(f"valor de la compra sin iva: ${precio:.2f}")
    print(f"iva (16%")
    return precio, iva, total
precio=float(input("ingrese el precio de compra: "))
iva= precio*0.16
total=precio+iva
print(f"valor de la compra sin iva: ${precio:.2f}")
print(f"iva (16%: ${iva:.2f}")
print(f"b¿valor de la compra con iva: ${iva:.2f}")