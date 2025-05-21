precio = float(input("Ingrese el precio del producto: "))
iva = 0.16 
total = precio * (1 + iva)

print(f"El precio con IVA incluido es: ${total:.2f}")
