import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="numero1"), sg.Text("+"),sg.Input(key="numero2"),sg.Text("=??")],
    [sg.Button("sumar")]

]
ventana = sg.Window("ejercicio S. Calculadora de suma simple", layout, font=('Bodoni MT', 20))
ventana.read()
ventana.close()