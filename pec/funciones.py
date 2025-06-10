def comparar_precios(p1, p2, p3, cantidad):
    precios = {
        "Tienda 1": p1,
        "Tienda 2": p2,
        "Tienda 3": p3
    }
    tienda_min = min(precios)
    precio_min = precios[tienda_min]
    ahorros = {}
    for tienda, precio in precios.items():
        if tienda != tienda_min:
            ahorro = (precio - precio_min) * cantidad
            ahorros[tienda] = round(ahorro, 2)

    return tienda_min, ahorros