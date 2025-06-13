import FreeSimpleGUI as sg
layout  = [
    [sg.Text("Ingrese nombre:"), sg.Input(key="nombre")],
    [sg.Text("Ingrese edad:"), sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito:"), sg.combo(["Python", "Javascript", " C++"])],
    [sg.Checkbox("Acepto recibir emails", key="email1")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
    ]
Window = sg.Window("Eventos: Ejemplo 04", layout, font=("Arial", 20))

while True:
    evento, valores = Window.read()
    if evento == "Enviar":
        nombre=valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguaje"]
        if valores["email1"]:
            recibe="Si"
        else:
            recibe="NO"