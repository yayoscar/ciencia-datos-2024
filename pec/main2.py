import FreeSimpleGUI as sg
import csv
from datetime import datetime

COLOR_FONDO_VENTANA = '#2E3B4E'
COLOR_TEXTO = '#E0F2F1'
COLOR_FONDO_INPUT = '#3A4B5F'
COLOR_TEXTO_INPUT = '#FFFFFF'
COLOR_BOTON_FONDO = '#5C6BC0'
COLOR_BOTON_TEXTO = '#FFFFFF'
COLOR_FONDO_MULTILINE = '#3A4B5F'
COLOR_TEXTO_MULTILINE = '#E0F2F1'

layout = [
    [sg.Text("Nombre del producto:", background_color=COLOR_FONDO_VENTANA, text_color=COLOR_TEXTO),
     sg.Input(key="objeto", background_color=COLOR_FONDO_INPUT, text_color=COLOR_TEXTO_INPUT)],

    [sg.Text("Precio en tienda 1:", background_color=COLOR_FONDO_VENTANA, text_color=COLOR_TEXTO),
     sg.Input(key="P1", background_color=COLOR_FONDO_INPUT, text_color=COLOR_TEXTO_INPUT)],

    [sg.Text("Precio en tienda 2:", background_color=COLOR_FONDO_VENTANA, text_color=COLOR_TEXTO),
     sg.Input(key="P2", background_color=COLOR_FONDO_INPUT, text_color=COLOR_TEXTO_INPUT)],

    [sg.Text("Precio en tienda 3:", background_color=COLOR_FONDO_VENTANA, text_color=COLOR_TEXTO),
     sg.Input(key="P3", background_color=COLOR_FONDO_INPUT, text_color=COLOR_TEXTO_INPUT)],

    [sg.Text("Cantidad a comprar:", background_color=COLOR_FONDO_VENTANA, text_color=COLOR_TEXTO),
     sg.Input(key="cantidad", background_color=COLOR_FONDO_INPUT, text_color=COLOR_TEXTO_INPUT)],

    [sg.Button("Comparar precios", button_color=(COLOR_BOTON_TEXTO, COLOR_BOTON_FONDO))],

    [sg.Multiline(size=(60, 6), key="resultado", disabled=True,
                  background_color=COLOR_FONDO_MULTILINE, text_color=COLOR_TEXTO_MULTILINE)]
]

window = sg.Window("Comparador de Precios Inteligente", layout, background_color=COLOR_FONDO_VENTANA)

def guardar_csv(producto, precios, cantidad, tienda_ganadora, ahorro):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("comparacion_precios.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([fecha, producto, *precios, cantidad, tienda_ganadora, ahorro])

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Comparar precios":
        try:
            producto = values["objeto"]
            cantidad = int(values["cantidad"])

            precios = []
            for key in ["P1", "P2", "P3"]:
                precio = values[key]
                if precio.strip() != "":
                    precios.append(float(precio))
                else:
                    precios.append(None)

            totales = []
            tiendas_validas_input = []
            for i, precio in enumerate(precios):
                if precio is not None:
                    totales.append(precio * cantidad)
                    tiendas_validas_input.append(precio)
                else:
                    totales.append(None)
                    tiendas_validas_input.append(None)

            tiendas_calculables = [(i+1, total) for i, total in enumerate(totales) if total is not None]

            if not tiendas_calculables:
                sg.popup_error("Error: Ingresa al menos un precio válido para comparar.")
                continue

            tienda_ganadora = min(tiendas_calculables, key=lambda x: x[1])
            tienda_mas_cara = max(tiendas_calculables, key=lambda x: x[1])

            ahorro_calculado = tienda_mas_cara[1] - tienda_ganadora[1]

            resultado = (
                f"Tienda recomendada: Tienda {tienda_ganadora[0]} (total: ${tienda_ganadora[1]:.2f})\n"
                f"Ahorro comparado con la más cara: ${ahorro_calculado:.2f}"
            )
            window["resultado"].update(resultado)

            guardar_csv(producto, tiendas_validas_input, cantidad, f"Tienda {tienda_ganadora[0]}", f"${ahorro_calculado:.2f}")

        except ValueError:
            sg.popup_error("Error: Verifica que todos los precios y la cantidad sean números válidos.")
        except Exception as e:
            sg.popup_error(f"Ha ocurrido un error inesperado: {e}")


window.close()