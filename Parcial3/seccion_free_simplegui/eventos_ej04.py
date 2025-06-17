import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese su nombre:"),sg.Input(key="nombre")],
    [sg.Text("Ingrese su edad:"),sg.Input(key="edad")],
    [sg.Text("Ingrese su lenguaje favorito: "),sg.Combo(["Python","Javascript","C++","Go","Java","C","C=","COBOL"],key="lenguaje")],
    [sg.Checkbox("Acepto recibir emails",key="email")],
    [sg.Button("Enviar"),sg.Button("Cancelar")]
]

window = sg.Window("Mini encuesta interactiva",layout,font=("Arial",22))

while True:
    evento,valores = window.read()
    if evento == "Enviar":
        nombre=valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguaje"]
        recibe = "Si" if valores["email"] else "No"
        mensaje =f"""Nombre: {nombre}
        Edad: {edad}
        Lenguaje favorito: {lenguaje}
        Recibe Emails: {recibe}"""
        sg.popup(mensaje,font=("Arial",25))
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

window.close()