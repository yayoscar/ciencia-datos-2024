import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre del producto:"),sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"),sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"),sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"),sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"),sg.Input(key="CANTIDAD")],
    [sg.Button("comparar precios:")]

]
ventana = sg.Window("ingrese el precio que quieres saber",layout,font=('Arial',20))

while True:
   evento, valores = ventana.read()
   if evento == sg.WINDOWCLOSE:
       break
   if evento == "ingresar precio":
       try:
ventana.read()
ventana.close()