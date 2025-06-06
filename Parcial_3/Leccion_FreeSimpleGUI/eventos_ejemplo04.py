import FreeSimpleGUI as sg

layout= [
    [sg.Text("Ingrese nombre:"), sg.Input(key= 'nombre')],
    [sg.Text("Ingrese edad:"), sg.Input(key= 'edad')],
    [sg.Text("Ingrese lenguaje favorito:"), sg.Combo(['Python', 'Javascript', 'C++', 'Java', 'C', 'C#', 'COBOL'], key="lenguaje")],
    [sg.Checkbox("Acepto recibir E-mails", key = "email")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]
window = sg.Window("Registro", layout, font=('Arial', 20))
while True:
    evento, values = window.read()
    if evento == "Enviar":
        nombre = values['nombre']
        edad = values['edad']
        lenguaje = values['lenguaje']
        recibe = "Sí" if values['email'] else "No"
        mensaje= f"""Nombre: {nombre}
        Edad: {edad}
        Lenguaje favorito: {lenguaje}
        Recibe e-mails: {recibe}"""
        sg.popup(mensaje)
    elif evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

window.close()