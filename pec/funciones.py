import FreeSimpleGUI as sg
import csv

def calcular_ahorro(precio, veces, meses):
    return precio * veces * meses * 4

def guardardatos(nombre, precio, veces, meses, total):
    archivo = "datos.csv"

    with open(archivo, "a+", newline="") as datos:
        datos.seek(0)
        contenido = datos.read()

    with open(archivo, "a", newline="") as datos:
        escritor = csv.writer(datos, delimiter=';')

        if contenido.strip() == "":
            escritor.writerow(["Nombre", "Precio", "Veces por semana", "Meses", "Total"])

        escritor.writerow([nombre, precio, veces, meses, total])

def calculadora(window):
    while True:
        event, values = window.read()

        if event == "calcular ahorro":
            try:
                nombre = values["nombre"]
                precio = float(values["precio"])
                veces = int(values["veces"])
                meses = int(values["meses"])

                total = calcular_ahorro(precio, veces, meses)
                resultado_texto = f"Podrías ahorrar ${total} en {meses} meses"
                window["resultado"].update(resultado_texto)

                guardardatos(nombre, precio, veces, meses, total)

            except:
                window["resultado"].update(" Verifica los datos.")

        if event == sg.WIN_CLOSED:
            break

    window.close()

