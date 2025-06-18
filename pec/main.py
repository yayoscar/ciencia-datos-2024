import FreeSimpleGUI as sg
from funciones import registro

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")],
]

window = sg.Window("Comparador de Precios Inteligente", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Comparar precios":
        try:
            producto_a_comprar = values["PRODUCTO"]
            cantidad_producto = int(values["CANTIDAD"])
            precios = []
            for key in ["P1", "P2", "P3"]:
                precio = values[key]
                if precio.strip() == "":
                    if key == "P3":
                        sg.popup_error("NO DEJES CASILLAS VACIAS AMOR,INTENTA DE NUEVO")
                        exit()
                    else:
                        precios.append(None)
                else:
                    precios.append(float(precio))
            costos = []
            for precio in precios:
                if precio is not None:
                    costos.append(precio * cantidad_producto)
            opciones_compra = []
            for indice, total in enumerate(costos):
                opciones_compra.append((indice + 1, total))
            if not opciones_compra:
                sg.popup_error("NO DEJES CASILLAS VACIAS AMORR")
                continue
            mejor_opción = min(opciones_compra, key=lambda x: x[1])
            peor_opción = max(opciones_compra, key=lambda x: x[1])
            mensaje_popup = (
                f"Tienda recomendada: Tienda {mejor_opción[0]} (total: ${mejor_opción[1]:.2f})\n"
                f"Ahorro comparado con la más cara: ${peor_opción[1] - mejor_opción[1]:.2f}"
            )
            sg.popup(mensaje_popup)
            registro(producto_a_comprar, precios, cantidad_producto, f"Tienda {mejor_opción[0]}", f"${peor_opción[1] - mejor_opción[1]:.2f}")
        except:
            window.close()