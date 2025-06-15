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