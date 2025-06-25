from funciones import registro
import FreeSimpleGUI as sg


layout = [
 [sg.Text("META DE AHORRO:", size=(20, 1), text_color="black"), sg.Input(key="META")],
 [sg.Text("NUMERO DE SEMANAS:", size=(20, 1), text_color="black"), sg.Input(key="SEMANAS")],
 [sg.Text("APORTE ACTUAL:", size=(20, 1), text_color="black"), sg.Input(key="APORTE")],
    [sg.Button("REGISTRAR APORTE", button_color=("white", "#28a745")), sg.Button("VER PROGRESO", button_color=("white", "#007bff"))],

 ]
window= sg.Window("Reto de Ahorro Personalizado",layout,font=("arial",20))

total_ahorrado = 0
while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        break

    if evento == "REGISTRAR APORTE":
        try:
            aporte = float(valores["APORTE"])
            total_ahorrado += aporte
            registro(aporte)
            sg.popup(f"Aporte registrado: ${aporte:.2f}\nTotal ahorrado: ${total_ahorrado:.2f}")
        except:
            sg.popup("Error: ingresa un valor numérico válido..")

    elif evento == "VER PROGRESO":
        try:
            meta = float(valores["META"])
            if meta == 0:
                sg.popup("La meta no puede ser 0.")
            else:
                progreso = (total_ahorrado / meta) * 100

                sg.popup(f"Llevas ahorrado el {progreso:.2f}% de tu meta.")
        except:
            sg.popup("Error: ingresa un valor válido para la meta.")

window.close()

