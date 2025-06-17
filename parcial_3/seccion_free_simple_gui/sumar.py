import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="numero1"),sg.Text("+"),sg.Input(key="numero2"),sg.Text("=???")],
    [sg.Button("Sumar")]
]

ventana = sg.Window("Ejercicio 5:Calculadorade suma simple",layout,font=("Arial",30))
lectura =ventana.read()
print(lectura)
ventana.close()