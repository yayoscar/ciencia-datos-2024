import FreeSimpleGUI as sg

layout = [
    [sg.Radio("Rock", "Grupo1", key="rock"),
     sg.Radio("Pop", "Grupo1", key="pop"),
     sg.Radio("Jazz", "Grupo1", key="jazz"),
     sg.Radio("Clásica", "Grupo1", key="clasica")],
    [sg.Button("Confirmar")]
]

window = sg.Window("Género Musical", layout, font=("Arial", 20))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Confirmar":
        if values["rock"]:
            genero = "Rock"
        elif values["pop"]:
            genero = "Pop"
        elif values["jazz"]:
            genero = "Jazz"
        elif values["clasica"]:
            genero = "Clásica"
        else:
            genero = "Ninguno seleccionado"

        sg.popup("Género seleccionado", f"Elegiste: {genero}")

window.close()