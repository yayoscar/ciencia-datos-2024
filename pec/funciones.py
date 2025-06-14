import csv
import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED
from datetime import datetime

def prepara_datos(valor):
    monto = valor['monto']
    categoria = valor['categoria']
    fecha = valor['fecha']
    if fecha == '':
        fecha = obtener_fecha()
    fila = [monto, categoria, fecha]
    return fila

def añade_csv(fila):
    with open("datos.csv", "a", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(fila)
    return True

def leer_dict():
    with open('datos.csv', 'r') as csvfile:
        campos = ['monto', 'categoria', 'fecha']
        lector = csv.DictReader(csvfile, fieldnames=campos)
        return lector

def comprobar(fila):
    valor = fila[0]
    while True:
        try:
            valor= float(valor)
            if float(valor).is_integer():
                valor = int(valor)
        except ValueError:
            sg.popup("No se puede guardar, el valor de monto debe ser un número", title="Error", background_color="#611227", font=("Cascadia Mono", 14), button_color="#EA9CB1")
            break
        ovalor = fila[1]
        if ovalor == str:
            ovalor = True
        if ovalor:
            return True
        else:
            sg.popup("No se puede guardar, debe poner la categoría", title="Error", background_color="#611227", font=("Cascadia Mono", 14), button_color="#EA9CB1")
            break
    return False


def leer_csv(nombre_archivo = 'datos.csv'):
    datos = []
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def mostrar_tabla():
    datos = leer_csv()
    layout2 = [
        [sg.Table(values=datos, headings=['Montos', 'Categorías', 'Fechas'], background_color="#EA9CB1", sbar_background_color="#8F1535", header_text_color="#BA4329", text_color="#8F1535")],
        [sg.Push(background_color="#ECAD83"), sg.Button("Limpiar", button_color="#8F1535"), sg.Button("Cerrar", button_color="#8F1535")]
    ]
    window = sg.Window("Registro", layout2, background_color="#ECAD83", font=("Cascadia Mono", 13))
    while True:
        evento, diccionario = window.read()
        if evento == "Cerrar" or evento == WIN_CLOSED:
            break
        elif evento == "Limpiar":
            borrar_registro()
            break
    window.close()


def borrar_registro():
    layout4 = [
        [sg.Text("¿Estás seguro de borrar todos los registros?", background_color="#BA4329")],
        [sg.Push(background_color="#BA4329"), sg.Button("Sí", button_color="#8F1535"), sg.Button("No", button_color="#8F1535")]
    ]
    ventana2 = sg.Window("Limpiar", layout4, font=("Cascadia Mono", 14), background_color="#BA4329")
    while True:
        evento, valores = ventana2.read()
        if evento == "Sí":
            with open("datos.csv", 'w', newline='') as archivo:
                limpiar = csv.writer(archivo)
                limpiar.writerows('')
            break
        else:
            break
    ventana2.close()

def hacer_resumen():
    datos = leer_csv()
    comida = 0
    salud = 0
    transporte = 0
    ropa_o_accesorios = 0
    impuestos = 0
    vivienda = 0
    otro = 0
    for fila in datos:
        if fila[1] == "Comida":
            comida += float(fila[0])
            if comida.is_integer():
                comida = int(comida)
        elif fila[1] == "Salud":
            salud += float(fila[0])
            if salud.is_integer():
                salud = int(salud)
        elif fila[1] == "Transporte":
            transporte += float(fila[0])
            if transporte.is_integer():
                transporte = int(transporte)
        elif fila[1] == "Ropa o accesorios":
            ropa_o_accesorios += float(fila[0])
            if ropa_o_accesorios.is_integer():
                ropa_o_accesorios = int(ropa_o_accesorios)
        elif fila[1] == "Impuestos":
            impuestos += float(fila[0])
            if impuestos.is_integer():
                impuestos = int(impuestos)
        elif fila[1] == "Vivienda":
            vivienda += float(fila[0])
            if vivienda.is_integer():
                vivienda = int(vivienda)
        elif fila[1] == "Otro":
            otro += float(fila[0])
            if otro.is_integer():
                otro = int(otro)
    total = comida+salud+transporte+ropa_o_accesorios+impuestos+vivienda+otro
    return comida, salud, transporte, ropa_o_accesorios, impuestos, vivienda, otro, total

def mostrar_resumen():
    comida, salud, transporte, ropa_o_accesorios, impuestos, vivienda, otro, total = hacer_resumen()
    layout3 = [
        [sg.Text("Gastos en Comida:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{comida}$", background_color="#B04461")],
        [sg.Text("Gastos en Transporte:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{transporte}$", background_color="#B04461")],
        [sg.Text("Gastos en Salud:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{salud}$", background_color="#B04461")],
        [sg.Text("Gastos en Ropa o accesorios:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{ropa_o_accesorios}$", background_color="#B04461")],
        [sg.Text("Gastos en Impuestos:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{impuestos}$", background_color="#B04461")],
        [sg.Text("Gastos en Vivienda:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{vivienda}$", background_color="#B04461")],
        [sg.Text("Gastos en Otros:", background_color="#B04461"),sg.Push(background_color="#B04461"), sg.Text(f"{otro}$", background_color="#B04461")],
        [sg.Text("Gastos totales:", background_color="#B04461"), sg.Push(background_color="#B04461"), sg.Text(f"{total}$", background_color="#B04461")],
        [sg.Push(background_color="#B04461"), sg.Button("Cerrar", button_color="#BA4329")]
        ]
    window2 = sg.Window("Resumen de gastos", layout3, font=("Cascadia Mono", 15), background_color="#B04461")
    while True:
        evento, diccionario = window2.read()
        if evento == "Cerrar" or evento == WIN_CLOSED:
            break
    window2.close()

def obtener_fecha():
    fecha_hoy = datetime.now()
    return fecha_hoy.strftime("%d/%m/%Y")

def borrar_campos(ventana):
    ventana["monto"].update("")
    ventana["categoria"].update("")
    ventana["fecha"].update("")
