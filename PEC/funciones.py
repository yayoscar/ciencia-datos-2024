import csv


def calcular_gasto(values):
    """
    Calcula el gasto total en un período de tiempo determinado.

    Args:
        values (dict): Diccionario con los valores de entrada.

    Returns:
        float: Gasto total en el período de tiempo determinado.
    """
    precio = float(values["PRECIO"])
    veces = int(values["VECES"])
    meses = int(values["MESES"])
    semanas_por_mes = 4
    gasto_semanal = precio * veces
    gasto_mensual = gasto_semanal * semanas_por_mes
    gasto_total = gasto_mensual * meses
    return gasto_total


def guardar_resultado(values, gasto_total):
    """
    Guarda el resultado en un archivo CSV.

    Args:
        values (dict): Diccionario con los valores de entrada.
        gasto_total (float): Gasto total calculado.
    """
    with open('datos.csv', 'a', newline='') as csvfile:
        fieldnames = ['nombre', 'precio', 'veces', 'meses', 'gasto_total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'nombre': values["NOMBRE"],
            'precio': values["PRECIO"],
            'veces': values["VECES"],
            'meses': values["MESES"],
            'gasto_total': gasto_total
        })


def mostrar_resultado(values, gasto_total):
    """
    Muestra el resultado en pantalla.

    Args:
        values (dict): Diccionario con los valores de entrada.
        gasto_total (float): Gasto total calculado.
    """
    resultado = f"Podrías ahorrar ${gasto_total:.2f} si evitas el gasto '{values['NOMBRE']}' por {values['MESES']} meses."
    return resultado