import FreeSimpleGUI as sg

layout = [
    [sg.Text("Selecciona tus aficiones:")],
    [sg.Checkbox("Leer", key="leer"),
     sg.Checkbox("Música", key="musica"),
     sg.Checkbox("Deportes", key="deportes")],
    [sg.Button("Mostrar selección")]
]

window = sg.Window("Aficiones", layout, font=("Arial", 20))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Mostrar selección":
        seleccionados = [hobby for hobby, marcado in values.items() if marcado]
        mensaje = "Tus aficiones:\n" + "\n".join(seleccionados) if seleccionados else "No seleccionaste ninguna."
        sg.popup(mensaje)

window.close()