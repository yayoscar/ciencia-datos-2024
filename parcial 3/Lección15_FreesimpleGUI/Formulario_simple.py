import FreeSimpleGUI as sg
layout=[
    [sg.Text("Nombre:"), sg.Input(key="NOMBRE")],
    [sg.Text("Edad:"), sg.Input(key="EDAD")],
    [sg.Button("Enviar"), sg.Button("cancelar")],
    [sg.Text("color favorito:"), sg.Combo(["Rojo", "Verde", "Azul"], key="COLOR")],
    [sg.Button("OK")],
    [sg.Text("Volumen:"), sg.Slider(range=(0, 100), orientation='h', key="VOLUMEN")]

]

Window = sg.Window("Formulario simple", layout, font=("Arial", 20))

Window.read()
Window.close()