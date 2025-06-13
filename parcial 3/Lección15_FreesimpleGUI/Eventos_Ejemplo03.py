import FreeSimpleGUI as sg

layout = [
    [sg.Text("¿Qué quieres hacer?")],
    [sg.Button("saludar 1"), sg.Button("saludar 2"), sg.Button("Salir")]
]

Window = sg.Window("Ejemplo 3: Multiple botones", layout, font=("Arial", 20))

while True:
    evento,valores = Window.read()
    if evento == "saludar 1":
        sg.popup("Hola este es un saludo")
    elif evento == "saludar 2":
        sg.popup("Este es otro saludo")
    elif evento == sg.WIN_CLOSED or evento=="Salir":
        break

    Window.close()
