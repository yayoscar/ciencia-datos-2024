import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese nombre:"), sg.Input(key="nombre")],
    [sg.Text("Ingrese edad"), sg.Input(key="edad")],
    [sg.Text("Lenguaje Favorito:"),sg.Combo(["Python","Javascript","C++","Go","COMBO"], key="lenguaje")],
    [sg.Checkbox("Acepto recibir emails",key="emails")],
    [sg.Button("Enviar"),sg.Button("Cancelar")]
]

window = sg.Window("Mini encuesta interactiva",layout,font=("Arial",20))

while True:
    evento ,valores = window.read()
    if evento == "Enviar":
        nombre = valores["nombre"]
        edad =  valores["edad"]
        lenguaje = valores["lenguaje"]
        recibe = "Si" if valores["email"] else "No"
        mensaje = """
        
        """
        sg.popup(mensaje,font=("Arial",20))
    if evento == sg.WIN_CLOSED or evento =="Cancelar":
        break

window.close()