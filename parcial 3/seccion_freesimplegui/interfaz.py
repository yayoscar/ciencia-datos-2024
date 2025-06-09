import verga as sg

layout = [
    [sg.Input(key="numero1"),sg.Text("+"),sg.Input(key="numero2"),sg.Text("=???")],
    [sg.Button("Sumar")]
]

ventana = sg.Window("Ejercicio 5: Calculadora de suma",layout,font=("Arial",20))

ventana.read()
ventana.close()