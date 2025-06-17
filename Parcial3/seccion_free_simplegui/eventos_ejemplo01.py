import FreeSimpleGUI as sg

layout = [
    [sg.Text("Nombre"),sg.Input(key="nmobre")],
    [sg.Button("Mostrar.",button_color=('lightblue','lightpink'))]
]

cositita = sg.Window("Mostrar nombre ingresado :)",layout,font=("Arial",20))

while True:
    event, values = cositita.read()
    if event == 'Mostrar':
        print(event,values)
        sg.popup(f"Tu nombre es {values['nombre']}",font=("Arial",20))
    elif event == sg.WIN_CLOSED:
        break

cositita.close()