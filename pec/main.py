#Importaciones
import FreeSimpleGUI as sg
import funciones as fd

#El diseño
layout = [
[sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO"), ],
[sg.Text("Precio en tienda 1:",text_color='red' ), sg.Input(key="P1")],
[sg.Text("Precio en tienda 2:",text_color='Black'), sg.Input(key="P2")],
[sg.Text("Cantidad a comprar:",text_color='green'), sg.Input(key="CANTIDAD")],
[sg.Button("Comparar precios"), sg.Button("Salir")]
]
#configurando la ventana
ventana = sg.Window("Encuesta", layout,font=("arial",20))
# eventos

while True:
    evento, valores = ventana.read()

    if evento == sg.WINDOW_CLOSED or evento == "Salir":
        break

ventana.close()