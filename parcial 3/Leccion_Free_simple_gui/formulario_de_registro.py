import FreeSimpleGUI as sg


layaut = [
    [sg.Text("nombre"), sg.Input(key="NOMBRE")],
    [sg.Text("apellido"), sg.Input(key="APELLIDO")],
    [sg.Text("gmail"), sg.Input(key="GMAIL")],
    [ sg.Button("LImpiar"),sg.Button("enviar")]

]

window = sg.Window("formulario de registro", layaut, font=("Arial",20))

window.read()
window.close()