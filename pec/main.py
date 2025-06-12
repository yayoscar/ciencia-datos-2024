# Llamando a la biblioteca y a las funciones
import FreeSimpleGUI as sg
from funciones import crear_csv, comparar

crear_csv()

# Asigno el Color de del mundo
sg.theme('BlueMono')

# La ventana
#El "size=" es para acomodar los cuadros
layout = [
    [sg.Text("Producto:", size=(20, 1)), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio tienda 1 :", size=(10, 1)), sg.Input(key="Precio 1")],
    [sg.Text("Precio tienda 2 :", size=(20, 1)), sg.Input(key="Precio 2")],
    [sg.Text("Cantidad a comprar:", size=(20, 1)), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar", button_color=("white", "green")), sg.Button("Salir", button_color=("white", "red"))],
    [sg.Text("", size=(50, 3), key="RESULTADO", text_color="Black")]
]

# Para centrar y llamar a la ventana
window = sg.Window("Comparador de Precios Inteligente", layout, element_justification='center')

# El ciclo del programa
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    if event == "Comparar":
        try:
            producto = values["PRODUCTO"]
            p1 = float(values["Precio 1"])
            p2 = float(values["Precio 2"])
            cantidad = int(values["CANTIDAD"])

            resultado, fila_csv = comparar(producto, p1, p2, cantidad)

            # Para mostrar el resultado
            window["RESULTADO"].update(resultado)

            # Para guardarlos en el CSV
            with open("datos.csv", "a", encoding="utf-8") as f:
                f.write(fila_csv + "\n")

        except (ValueError, TypeError):
            sg.popup("Revisa bien los datos.")

window.close()
