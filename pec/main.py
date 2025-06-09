import FreeSimpleGUI as sg
from funciones import *



layout = [
[sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
[sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
[sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
[sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
[sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
[sg.Button("Comparar precios")],
[sg.Text("tienda recomendada")],
[sg.Text("total a pagar")],
[sg.Text("ahorro respectivo alas demas tiendas ")]
]

window = sg.Window("Proyecto 5", layout,font=("Arial",20))
window.read()
window.close()
print(comparar_precios())