import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="numero1"),sg.Text("."),sg.Input(key="numero2"),sg.Text("= ??")],
[sg.Button("sumar")]

]

ventana = sg.Window("ejercicio 5: calculadora de suma simple",layout,font=("Arial",15))

lectura = ventana.read()
print(lectura)
ventana.close()
