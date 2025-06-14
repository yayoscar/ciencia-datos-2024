import FreeSimpleGUI as sg
layout=[
    [sg.Text("Ingrese nombre: "),sg.Input(key="nombre")],
    [sg.Text("Ingrese edad: "),sg.Input(key="edad")],
    [sg.Text("Ingrese su lenguaje de programacion favorito: "),sg.Combo(["Python","Javascript","C++","Go","Java"],key="lenguaje")],
    [sg.Checkbox("Acepto recibir emails")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]

window = sg.Window("Mini encuesta interactiva",layout,font=("Arial",20))
while True:
    evento,valores=window.read()
    if evento=="Enviar":
        nombre = valores["nombre"]
        edad = valores["edad"]
        lenguaje=valores["lenguaje"]
        recibe = "Si" if valores["email"] else "No"
        mensaje = f"""Nombre: {nombre}
        edad: {edad}
        lenguaje favorito: {lenguaje}
        Recibe Emails: {recibe}"""
        sg.popup(mensaje,font=("Arial",20))
        if evento == sg.WIN_CLOSED or evento=="Cancelar":
            break

window.close()