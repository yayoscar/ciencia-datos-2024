import FreeSimpleGUI as sg

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar reporte:"), sg.Button(key="ver progreso")]
]

Window = sg.Window("Reto de ahorro personalizado", layout, font=("Arial", 20))
while True:
    evento,valores = Window.read()
    if evento == "Registrar reporte":
        Meta_ahorro=valores["META"]
        Num_semanas=valores["SEMANAS"]
        Aporte_actual=valores["APORTE"]
    if evento == "ver progreso":
        ver_progreso = valores["META", "SEMANAS", "APORTE"]
        if evento:
            datos=("El usuario ha ingresado sus datos")
        else:
            datos=("El usuario aun no completa los datos que se piden.")
        sg.popup(f"{datos}, y ha decidido {evento['Registrar reporte']} o {evento['Ver progreso']}")

    elif evento == sg.WIN_CLOSED:
        break

    Window.close()



