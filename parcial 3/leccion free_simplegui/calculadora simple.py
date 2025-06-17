import FreeSimpleGUI as sg

layout=[
    [sg.Input(key="n1")],
    [sg.Input(key="n2")],
    [sg.Button("sumar"),sg.Button("resta"),sg.Button("multiplicacion"),sg.Button("division")],
    [sg.Button("potencia")],
    [sg.Button("cerrar")],
    [sg.Text("resultado:",key="respuesta")]
]

window=sg.Window("calculadora basica", layout)


while True:
   try:
        event, values =window.read()
        valor1 = int(values["n1"])
        valor2 = int(values["n2"])

        if event=="sumar":
                suma=valor1+valor2
                window["respuesta"].update(f"la suma es: {suma}")
        elif event =="resta":
                resta=valor1-valor2
                window["respuesta"].update(f"el resultado de la resta es: {resta}")
        elif event =="multiplicacion":
                multiplicar=valor1*valor2
                window["respuesta"].update(f"el resultado de la multiplicacion es: {multiplicar}")
        elif event == "division":
                dividir=valor1/valor2
                window["respuesta"].update(f"el resultado de la division es: {dividir}")
        elif event == "potencia":
            cuadrado=valor1**valor2
            window["respuesta"].update(f" el resultado de la potencia es {cuadrado}")
        if event == "sg.WIN_CLOSED" or event == "cerrar":
            break
   except ValueError:
        sg.popup_error("ingrese un numero")

