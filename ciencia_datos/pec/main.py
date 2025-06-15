import FreeSimpleGUI as sg

from ciencia_datos.pec.funciones import registro

layout = [
 [sg.Text("META DE AHORRO:"), sg.Input(key="META")],
 [sg.Text("NUMERO DE SEMANAS:"), sg.Input(key="SEMANAS")],
 [sg.Text("APORTE ACTUAL:"), sg.Input(key="APORTE")],
 [sg.Button("REGISTRAR APORTE"), sg.Button("VER PROGRESO")]
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
            sg.popup("se ha registrado correctamente.")

    elif evento == "VER PROGRESO":
        try:
            meta = float(valores["META"])
            if meta ==(valores["META"])
                sg.popup("La meta no puede ser 0.")
            else:
                progreso = (total_ahorrado / meta) * 100

                sg.popup(f"Llevas ahorrado el {progreso:.2f}% de tu meta.")
        except:
            sg.popup("Error: ingresa un valor válido para la meta.")

window.close()

