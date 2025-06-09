import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese nombre:"), sg.Input(key="nombre")],
    [sg.Text("Ingrese edad:"), sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito:"), sg.Combo(["Python", "Javascript", "C++"], key="lenguaje")],
    [sg.Checkbox("Acpeto recibir emails", key="email")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]

window = sg.Window("Ejemplo04 - Encuesta interactiva", font=("Arial", 20))

while True:
    evento, valores = window.read()
    if evento == "Enviar":
        nombre = valores["nombre"]
        edad = valores["edad"]
        lenguaje = valores["lenguaje"]
        recibe = "Si" if valores["email"] else "No"
        mensaje = f"""Nombre:{nombre}
        Edad:{edad}
        Lenguaje favorito:{lenguaje}
        Recibe emails:{recibe}"""
        sg.popup(mensaje, font=("Arial", 20))
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

window.close()