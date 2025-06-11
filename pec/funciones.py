import FreeSimpleGUI as sg


layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar aporte"), sg.Button("Ver progreso")]
    ]
window=sg.Window("Reto de ahorro", layout, font=("Arial",15))
while True:
    event, values =window.read()
    if event=="Registrar aporte":
        print(event,values)
        sg.popup(f"tu meta de ahorro es:{values["Aporte"]}")
    elif event==sg.WIN_CLOSED:
        break
window.close()

