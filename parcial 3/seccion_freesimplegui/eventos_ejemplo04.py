import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese nombre: "),sg.Input(key="nombre")],
    [sg.Text("Ingrese edad: "), sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito: "), sg.Combo(['Python','Javascript','C++','Go','Java'],key="LENGUAJE")],
    [sg.Checkbox("Acepto recibir emails",key="email")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]

window = sg.Window("Mini encuesta interactiva",layout,font=("Arial",20))

while True:
    evento, valores = window.read()
    if evento == "Enviar":
        nombre = valores["nombre"]
        edad = valores["edad"]
        lenguaje = valores["LENGUAJE"]
        recibe = ("Si") if valores["email"] else "No"
        mensaje = f"""Nombre: {nombre}
        edad: {edad}
        lenguaje favorito: {lenguaje}
        recibe emails: {recibe}"""
        sg.popup(mensaje,font=("Arial",20))
    if evento == sg.WIN.CLOSED or evento == "Cancelar":
        break