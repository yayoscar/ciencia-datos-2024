def comparar_precios(p1, p2, p3, cantidad):
    precios = {
        "Tienda 1": p1 * cantidad,
        "Tienda 2": p2 * cantidad,
        "Tienda 3": p3 * cantidad
    }
    tienda_min = min(precios, key=precios.get)
    precio_min = precios[tienda_min]
    precio_max = max(precios.values())
    ahorro = precio_max - precio_min
    return tienda_min, precio_min, ahorro