import FreeSimpleGUI as sg

layout = [
 [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
 [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
 [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
 [sg.Button("Registrar aporte o aportes"), sg.Button("Ver progreso")]
 ]

window = sg.Window("Meta de ahorro",layout,font=("Harlow Solid Italic",25))

while True:
    event, values = window.read()
    if event == "Mostrar lista de meta de ahorro":
        print(event,values)
        sg.popup(f"Tu lista de ahorros es {values["hasta el momento"]}")

    elif event == sg.WIN_CLOSED:
        break
print(sg.Button)
window.close()