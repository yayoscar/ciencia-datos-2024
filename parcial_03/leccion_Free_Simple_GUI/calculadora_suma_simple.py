import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="numero1"),sg.Text("+"),sg.Input(key="numero2"),sg.Text("= ??")],
    [sg.Button("sumar")]

]

ventana = sg.Window("ejemplo 5: Calculadora de suma simple",layout,font=('Arial',10))

ventana.read()
ventana.close()