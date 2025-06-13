import FreeSimpleGUI as sg

from pec.funciones import guardar_en_csv, leer_csv

layout = [
 [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
 [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
 [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
 [sg.Button("Registrar aporte o aportes"), sg.Button("Ver progreso")],
 [sg.Button("acaptar poner 10 en general a estrellita")],
 [sg.Image(sg.EMOJI_BASE64_COOL)]
 ]

window = sg.Window("Meta de ahorro",layout,font=("Harlow Solid Italic",25))

while True:
    event, values = window.read()
    if event == "Mostrar lista de meta de ahorro":
        print(event,values)
        sg.popup(f"Tu lista de ahorros es {values["hasta el momento"]}")
    elif event == "Registrar aporte o aportes":
        fila = [values["APORTE"]]
        guardar_en_csv(fila)
    elif event == "Ver progreso":
        leer_csv()
    elif event == sg.WIN_CLOSED:
        break
print(sg.Button)
window.close()