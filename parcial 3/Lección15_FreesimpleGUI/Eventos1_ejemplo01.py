import FreeSimpleGUI as sg
layout=[
    [sg.Text("Nombre"), sg.Input(key="Nombre")],
    [sg.Button("Mostrar")]
]

Window = sg.Window("Evento:Ejercicio01", layout,font=("Arial",20))

while True:
    event, values = Window.read()
    if event == "Mostrar":
        sg.poup(f"Tu nombre es {values['Nombre']}")
    elif event == sg.WIN_CLOSED:
     break

Window.close()

