import FreeSimpleGUI as sg


def precios_comparados(precio, cantidad ):
    try:
        cantidad = float(cantidad)
        total = [float(precio) * cantidad for precio in precio]
        tienda_mas_barata = total.index(min(total)) + 1
        return (f"La tienda mas barata es: {tienda_mas_barata} con un total de {min(total):.2f}")
    except ValueError:
            return "Por favor, ponga solo numeros"


layout = [
        [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
        [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
        [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
        [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
        [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
        [sg.Button("Comparar precios:")]
]

window = sg.Window("tienda en donde me conbiene comprar",layout)
while True:
    evento,valores=window.read()
