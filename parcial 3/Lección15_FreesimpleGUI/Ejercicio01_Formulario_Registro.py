import FreeSimpleGUI as sg
layout=[
    [sg.Text("Nombre:"), sg.Input("NOMBRE")],
    [sg.Text("Apellido:"), sg.Input("APELLIDO")],
    [sg.Text("Email:"), sg.Input("EMAIL")],
    [sg.Button("Enviar"), sg.Button("limpiar")]
    ]

Window = sg.Window("Ejercicio01_Formulario_Registro", layout, font=("Arial", 20))

Window.read()
Window.close()