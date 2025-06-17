import FreeSimpleGUI as sg

layout = [
    [sg.Text("ingrese nombre:"),sg.Input(key="nombre")],
    [sg.Text("ingrese su edad"),sg.Input(key="edad")],
    [sg.Text("lenguaje favorito:"),sg.Combo(["Python","Javascript","c++","Bo","Java"],key="lenguaje")],
    [sg.Checkbox("Acepto recibir Emails",key="Email")],
    [sg.Button("Enviar"),sg.Button("cancelar")]
]

window = sg.Window("Mini encuesta interactiva",layout,font=("Arial",20))

while True:
    evento, valores = window.read()
    if evento=="enviar":
        nombre=valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguaje"]
        if valores["email"]:
            recibe="Si"
        else:
            recibe=("No")
        recibe = "Si" if valores["email"] else "No"
        mensaje = f"""Nombre: {nombre}
        edad: {edad}
        lenguaje favorito: {lenguaje}
        Recibe Emails: {recibe}"""
        sg.popup(mensaje,font=("Arial",20))
    if evento == sg.WIN_CLOSED or evento == "cancelar":
        break

window.close()
