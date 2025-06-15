import csv


def guardar_aporte(meta, semanas, aporte):

    with open("datos.csv", mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([meta, semanas, aporte])


def calcular_progreso(meta, semanas):

    total_ahorrado = 0
    aportes_realizados = 0

    with open("datos.csv", mode="r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            total_ahorrado += int(fila[2])
            aportes_realizados += 1

    porcentaje = (total_ahorrado / int(meta)) * 100
    faltante = int(meta) - total_ahorrado

    if aportes_realizados == 0:
        estado = "Aún no has comenzado el ahorro. ¡Empieza hoy!"
    elif porcentaje >= 100:
        estado = "¡Meta cumplida! Felicidades 🎉"
    elif aportes_realizados < int(semanas) / 2:
        estado = "Vas un poco lento, pero puedes mejorar 💪"
    else:
        estado = "Vas en buen camino, sigue así 👍"

    return total_ahorrado, faltante, round(porcentaje, 2), estado
