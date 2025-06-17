import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿Que quieres hacer")],
    [sg.Button("Saludar 1"), sg.Button("saludar 2"), sg.Button("saludar 3")]
]

Window = sg.Window("Ejemplo 3: Multiples botones",layout,font=("Arial, 12"))

while True:
    evento,valores = Window.read()
    if evento == "saludar 1":
        sg.Popup("Hola este es un saludo mas")
    elif evento == "saludar 2":
        sg.Popup("Este es otro saludo")
    elif evento == sg.WIN_CLOSED or evento=="salir":
        break

Window.close()