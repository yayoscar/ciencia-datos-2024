import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="numero1"),sg.Text("+"),sg.Input(key="numero2"),sg.Text("= ??")],
    [sg.Button("Sumar")]
]

cosita = sg.Window("Calculadora de suma simple.",layout,font=("Arial",20))

lectura = cosita.read()
print(lectura)
cosita.close()