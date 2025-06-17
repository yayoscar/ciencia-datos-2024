import FreeSimpleGUI as sg
layout = [
    [sg.Text("nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad: "), sg.Input(key="EDAD")],
    [sg.Button("Enviar"), sg.Button("cancelar")]

]
window = sg.window("formulario Simple" ,layout, front=("arial", 20))
window.read()
window.close()
