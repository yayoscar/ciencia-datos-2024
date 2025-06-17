def precios_comparados(precio , cantidad):
    try:
        cantidad = float(cantidad)
        total = [float(precio) * cantidad for precio in precio]
        tienda_mas_barata = total.index(min(total)) + 1
        return (f"La tienda mas barata es: ¨{tienda_mas_barata} con um total de {min(total):.f}")
    except ValueError:
        return "por favor , ponga solo numeros"