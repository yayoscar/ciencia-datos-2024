from funciones import comparador
import FreeSimpleGUI as sg


layout = [
[sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precio")],
    [sg.Multiline(size=(20, 3), key="RESULTADO", disabled=True)]


]
ventana = sg.Window("Comparador de precios",layout,font=('Arial',20))

while True:
   evento, valores = ventana.read()
   if evento == sg.WINDOWCLOSE:
       break
   if evento == "ingresar precio":
       try:
        producto = valores["PRODUCTO"]
       cantidad = int(valores["CANTIDAD"])
       precios = []

       precio = float(valores["precio"])
       precio_producto =- precio
       comparador(precio)
       sg.popup(f"precio en tienda es: {precio: .1f},{precio: .2f},{precio: .3f}"),
   else:
       sg.popup("verifica los datos ingresados.")

ventana.close()