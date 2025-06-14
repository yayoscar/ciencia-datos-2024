import FreeSimpleGUI as sg



layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="NOMBRE")],
    [sg.Text("Precio por unidad:"), sg.Input(key="PRECIO")],
    [sg.Text("Veces por semana:"), sg.Input(key="VECES")],
    [sg.Text("Meses:"), sg.Input(key="MESES")],
    [sg.Button("Calcular ahorro")],
    [sg.Text("Resultados:", font=("Arial", 12, "bold"))],
    [sg.Multiline(size=(50, 10), key="RESULTADO", disabled=True)]
]
