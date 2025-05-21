total_compra = float(input("ingresa el monto total de la compra:$"))
dinero_entregado =float(input("ingresa la cantidad de dinero entregada por el cliente:$"))
if dinero_entregado < total_compra:
    print("error: el dinero entregado no es suficiente para cubrir la compra.")
else:
    print("El dinero entregado no es suficiente para cubrir la cpmpra.")
    cambio = dinero_entregado - total_compra
    print(f"El cambio a antregar al cliente es:{cambio:.2f}$")