import FreeSimpleGUI as sg
from funciones import guardar_en_csv, leer_csv

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("PROGRESO"), sg.Button("GUARDAR")],
    [sg.Image(sg.EMOJI_BASE64_COOL)]
]

window = sg.Window("Meta de ahorro", layout, font=("Arial", 30))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "GUARDAR":
        if values["META"] and values["SEMANAS"] and values["APORTE"]:
            guardar_en_csv(values["META"], values["SEMANAS"], values["APORTE"])
            sg.popup("listo", "todo bien guardadito")
        else:
            sg.popup_error("Error", "llena todos los campos(lugares para escribir)")

    elif event == "PROGRESO":
        datos = leer_csv()
        if not datos:
            sg.popup("Aviso", "Nopis ningun dato guardado")
        else:
            texto = "Ahorros:\n\n"
            for fila in datos:
                texto += f"Meta: ${fila[0]} | Semanas: {fila[1]} | Aporte: ${fila[2]}\n"
            sg.popup("Progreso", texto)

window.close()