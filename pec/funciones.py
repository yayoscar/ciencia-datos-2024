import FreeSimpleGUI as sg
import csv
def crear(archivo):
    try:
        with open(archivo, "r") as f:
            pass
    except FileNotFoundError:
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Monto Inicial", "Ahorro Mensual", "Meses", "Banco", "Resultado"])

def guardar_datos(archivo,values):
    try:
        with open(archivo, "a", newline="") as f:
            writer=csv.writer(f)
            writer.writerow(values)
        sg.popup("Datos guardados correctamente")
    except Exception as e:
        sg.popup("Error al guardar datos:", str(e))

def calculo(tasa_mensual,meses,ahorro_mensual,monto_inicial):
    monto_final=monto_inicial*(1+tasa_mensual)**meses+ahorro_mensual*(((1+tasa_mensual)**meses-1)/tasa_mensual)
    resultado=f"Tendrias {monto_final} al finalizar los {meses} meses"
    return resultado
def ventana():
    layout = [
        [sg.Text("Monto inicial:", background_color="#4b5861"), sg.Input(key="INICIAL", background_color="#f6f2e6")],
        [sg.Text("Ahorro mensual:", background_color="#4b5861"), sg.Input(key="MENSUAL", background_color="#f6f2e6")],
        [sg.Text("Meses:", background_color="#4b5861"), sg.Input(key="MESES", background_color="#f6f2e6")],
        [sg.Text("Banco:", background_color="#4b5861"),
         sg.Combo(["Hey Banco", "NU", "Finsus"], key="BANCO", background_color="#293b3d", text_color="#a8bcba")],
        [sg.Button("Calcular", button_color="#4b5861")], [sg.Button("Cerrar", button_color="#4b5861")]
    ]

    ventana = sg.Window("Ahorro en bancos digitales", layout, icon="JaneDoeChibi.ico",
                        background_color="#839d9e")  # Le agregue icono y color
    return ventana