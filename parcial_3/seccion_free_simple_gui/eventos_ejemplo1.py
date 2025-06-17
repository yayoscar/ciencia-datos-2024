import FreeSimpleGUI as sg

layout =[
    [sg.Text("Nombre"),sg.Input(key="NOMBRE",)],
    [sg.Button("Mostrar",button_color='pink')]

]
window = sg.Window("Mostrar nombre ingresado",layout,font=("Arial",30))

while True:
    event, values = window.read()
    if event == "Mostrar":
        print(event,values)
        sg.popup(f"Hola, tu nombre es: {values['NOMBRE']}")
    elif event == sg.WIN_CLOSED:
        break
window.close()