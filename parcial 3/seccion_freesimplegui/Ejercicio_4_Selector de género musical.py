import FreeSimpleGUI as sg

layout = [
    [sg.Text("Selecciona tu género musical favorito:")],
    [sg.Radio("Rock", "GENERO", key="ROCK"),
     sg.Radio("Pop", "GENERO", key="POP"),
     sg.Radio("Jazz", "GENERO", key="JAZZ"),
     sg.Radio("Clásica", "GENERO", key="CLASICA")],
    [sg.Button("Confirmar")]
]

window = sg.Window("Selector Musical", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,):
        break
    elif event == "Confirmar":
        for key, selected in values.items():
            if selected:
                sg.popup(f"Género seleccionado: {key}")
                break

window.close()
