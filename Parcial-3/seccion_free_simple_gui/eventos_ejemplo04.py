import FreeSimpleGUI as sg

layout = [
    [sg.Text("ingrese nombre:"),sg.Input(key="nombre")],
    [sg.Text("Edad:"), sg.Input(key="edad")],
    [sg.Text("Lenguaje Favorito"), sg.Combo(["Python","Javascript","C++"],key="lenguajes")],
    [sg.Checkbox("Acepto ecibir Emails", key="email")],
    sg.Button("Enviar"), sg.Button("Cancelar")
]


window = sg.Window("Mini encuesta innteractiva",layout,font=("Arial",20))

while True:
    event, valores = window.read()
    if event == "Enviar":
        nombre =valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguajes"]
        recibe = "Si" if valores ["email"] else "No"
        mensaje = f"""Nombre: {nombre}
                    edad: {edad}
                    Recibe emails{recibe}"""
        sg.popup()