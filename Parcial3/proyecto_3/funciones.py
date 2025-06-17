def calcular_ahorro(nombre_gasto, precio_unidad, veces_por_semana, meses):
    try:
        precio = float(precio_unidad)
        veces = int(veces_por_semana)
        meses = int(meses)

        ahorro = precio * veces * 4 * meses
        #Aquí, para obtener una cifra más exacta sobre las veces de las semanas en los meses, se usaría 4.33, sin embargo, para
        #la salida que pide el proyecto, es más adecuado usar solo el número 4.
        mensaje = (f"Con ese gasto, gastas ${ahorro:.2f} en tan solo {meses} meses. "
                   f"Si dejaras de consumir '{nombre_gasto}' a ${precio} por unidad, "
                   f"{veces} veces por semana durante {meses} meses, ahorrarías aproximadamente ${ahorro:.2f}.")
    except ValueError:
        mensaje = "Por favor, asegúrate de ingresar solo números válidos en los campos numéricos."

    return mensaje