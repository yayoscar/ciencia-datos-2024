import FreeSimpleGUI as sg

layout = [
    [sg.Text("ingrese nombre"),sg.Input(key="nombre")],
    [sg.Text("ingrese edad"),sg.Input(key="edad")],
    [sg.Text("lenguaje favorito: "),sg.Combo(values=["Phyton","javascrpit","C++","Go","Java"],key='Lenguaje')],
    [sg.Checkbox(text="acepto recibir emails",key="emails")],
    [sg.Button("enviar"),sg.Button("cancelar")],
    [sg.Button("enviar"),sg.Button("cancelar")]

]

window= sg.Window("mini encuesta interactiva",layout,font=("Arial",20))

while True:
    evento, valores = window.read()
    if evento=="enviar":
        nombre=valores["nombre"]
        edad=valores=["edad"]
        lenguaje=valores["lenguaje"]
        recibe = "si" if valores["emails"] else "no"
        mensaje = f"""Nombre: {nombre}
        edad: {edad}
        lenguaje favorito: {lenguaje}
        recibe emails: {recibe}"""
        sg.popup(mensaje,font=("Arial",20))
        if evento == sg.WIN_CLOSED or evento == "cancelar":
            break

window.close()