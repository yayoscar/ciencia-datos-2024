import FreeSimpleGUI as sg

def calcular_ahorro(precio, veces, meses):
    return precio * veces * meses * 4

def calculadora(window):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "calcular ahorro":
            try:
                precio = int(values["precio"])
                veces = int(values["veces"])
                meses = int(values["meses"])
                total = calcular_ahorro(precio, veces, meses)
                window["resultado"].update(f"podrias ahorrar ${total:} si evitas este gasto por {meses} meses")
            except:
                window["resultado"].update("error verifica los datos")

    window.close()


