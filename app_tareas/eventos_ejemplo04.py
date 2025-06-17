import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED

layout =[
    [sg.Text("Ingrese nombre:"),sg.Input(key="nombre")],
    [sg.Text("Ingrese edad:"),sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito:"),sg.Combo(["Python","C++","Go","Java", "C#", "COBOL"]]
    [sg.Checkbox("Acepto resibir analisis", key="email")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]
Window = sg.Window("Mini encuesta interactiva",layout,font=("Arial, 20"))

while True:
    evento, valores = Window.read()
    if evento =="Enviar":
        nombre=valores["Nombre"]
        edad=valores["edad"]
        lenguaje==valores["lenguaje"]
        if valores["email"]:
            recibe="SI" if valores["email"] else "No"
            mensaje = f"""Nombre" {nombre}
            edad: {edad}
            lenguaje favorito: {lenguaje}
            Recibe Emails: {recibe}"""
            sg.Popup(mensaje,font=)
        if evento == sg.WIN_CLOSED or evento == "cancelar":
            break
Window.close()