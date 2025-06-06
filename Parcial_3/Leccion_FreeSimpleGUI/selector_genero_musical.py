import FreeSimpleGUI as sg

layout= [
    [sg.Radio('Rock', 'GRUPO', key="Rock"), sg.Radio('Pop', 'GRUPO', key="Pop"), sg.Radio('Jazz', 'GRUPO', key="Jazz"), sg.Radio('Clásica', 'GRUPO', key="Clasica")],
    [sg.Button('Confirmar', button_color="dark green")]
]
window = sg.Window("Selector de género musical", layout, font=("Arial", 20))

window.read()
window.close()