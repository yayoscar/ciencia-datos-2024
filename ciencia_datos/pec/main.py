import FreeSimpleGUI as sg

layout = [
 [sg.Text("META DE AHORRO:"), sg.Input(key="META")],
 [sg.Text("NUMERO DE SEMANAS:"), sg.Input(key="SEMANAS")],
 [sg.Text("APORTE ACTUAL:"), sg.Input(key="APORTE")],
 [sg.Button("REGISTRAR APORTE"), sg.Button("VER PROGRESO")]
 ]
window= sg.Window("Reto de Ahorro Personalizado",layout,font=("arial",20))

window.read()
window.close()