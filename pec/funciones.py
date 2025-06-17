def validar_monto(monto_str):
    """
     convierte el monto de texto a float.
     Devuelve el numero o Nada si no es válido.
    """
    try:
        return float(monto_str)
    except ValueError:
        return None

def guardar_gasto(gastos, monto, categoria, fecha):
    """
    Agrega un gasto a la lista gastos.
    """
    gastos.append({
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha
    })

def calcular_resumen(gastos):
    """
    Calcula el total de gastos por categoría.
    Devuelve un diccionario con categoría: total.
    """
    resumen = {}
    for gasto in gastos:
        quepongoxd = gasto["categoria"]
        resumen[quepongoxd] = resumen.get(quepongoxd, 0) + gasto["monto"]
    return resumen
#Perdon si puse quepongoxd de variable es que no tenia ningun tipo de cosa en la cabeza para ponerle de nombre a la variable