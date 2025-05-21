
print("1. Calcular IVA")
print("2. Salir")

opcion = input("Ingrese una opción: ")

if opcion == "1":
    valor_compra = float(input("Ingrese el valor de la compra sin IVA: "))
    iva = valor_compra * 0.16
    valor_total = valor_compra + iva

    print(f"Valor de la compra sin IVA: {valor_compra:.2f}")
    print(f"IVA (16%): {iva:.2f}")
    print(f"Valor total con IVA: {valor_total:.2f}")
elif opcion == "2":
    print("Saliendo del programa")
else:
    print("Opción inválida, intente de nuevo.")
