import FreeSimpleGUI as sg
def casita():
    if accion["Gryffindor"]:
        return "Gryffindor"
    elif accion["Slytherin"]:
        return "Slytherin"
    elif accion["Ravenclaw"]:
        return "Ravenclaw"
    else:
        return "Hufflepuf"
layout = [
    [sg.Text("Nombre:"), sg.Input(k= "nombre")],
    [sg.Text("¿De qué casa eres?",p=(10,10)), sg.Text()],
    [sg.Radio("Gryffindor", "c", key="Gryffindor"), sg.Radio("Slytherin", "c",key="Slytherin"), sg.Radio("Ravenclaw", "c",key="Ravenclaw"), sg.Radio("Hufflepuf", "c",key="Hufflepuf")],
    [sg.Button("Ok", key="casa")]
]
ventana = sg.Window("Ventana", layout, font=("Sitka", 15))
while True:
    evento, accion = ventana.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == "casa":
        sg.popup(f"Felicidades {accion['nombre']}, eres {casita()}!")


ventana.close()
