import FreeSimpleGUI as sg

layout = [
    [sg.Text("Selecciona tus hobbies:")],
    [sg.Checkbox("Leer", key="Leer"),
     sg.Checkbox("Viajar", key="Viajar"),
     sg.Checkbox("Programar", key="Programar")],
    [sg.Button("Mostrar selección")]
]

window = sg.Window("Hobbies", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Mostrar selección":
        hobbies = [hobby for hobby, selected in values.items() if selected]
        sg.popup("Seleccionaste: " + ", ".join(hobbies))

window.close()
