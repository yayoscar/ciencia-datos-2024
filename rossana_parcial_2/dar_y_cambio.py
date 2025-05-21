total_compra = float(input("ingresa el monto de su compra:$"))
dinero_entregado = float(input("ingresa la cantidad de dinero entregado por su cliente:$"))
if dinero_entregado < total_compra:
    print("el dinero entregado no es suficiente para cubrir la compra.")
else:
    print("el dinero entregado es suficiente para cubrir la compra.")
    cambio = dinero_entregado - total_compra
    print(f"el cambio a entregar el cliente es {cambio:2f}$")