import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre"), sg.Input(key="NOMBRE")],
    [sg.Button("Mostrar")]
]

window = sg.Window('Nombre ingresado', layout, font=('Arial', 30))
while True:
    event, values = window.read()
    if event == "Mostrar":
        sg.popup(f"Hola! Tu nombre es {values["NOMBRE"]}", font=('Arial', 20))
    elif event == sg.WIN_CLOSED:
        break

window.close()