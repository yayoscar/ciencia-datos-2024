from collections import defaultdict
from pec.funciones import leer_gastos_desde_csv
import FreeSimpleGUI as sg
import os
from pec.funciones import datos_csv
from datetime import datetime
from pec.funciones import verificar_archivo



sg.theme('LightBlue3')
layout = [
    [sg.Text("Proyecto pec:",pad=(300,20),font=('Arial',40))],
    [sg.Text(" Monto del gasto :",pad=(0,20),font=('Arial',20)),sg.Input(key='MONTO',size=(22,0))],
    [sg.Text("    Categoria:  "),sg.Combo(['Comida','Transporte','Electricidad','Salidas','Viajes','Compras','otros'],size=(21,0),pad=(40,10),key='CATEGORIA')],
    [sg.Text(' Fecha (opcional):',pad=(0,20)),sg.Input(key='FECHA',size=(22,0))],
    [sg.Button("Guardar gasto",button_color=('White','blue')),
     sg.Button("Ver resumen",button_color=('White','green')),
     sg.Button('Ver registros',button_color=('White','yellow')),
     sg.Button('Salir',button_color=('White','red'))]

]
window = sg.Window("Proyecto pec", layout,font=('Arial',20))

archivo_csv = 'datos.csv'
datos_usuario = ['Monto del gasto','Categoria','Fecha(opcional)']
verificar_archivo(archivo_csv, datos_usuario)



while True:
    evento,values = window.read()
    if evento == sg.WIN_CLOSED or evento == 'Salir':
        sg.popup('¡Gracias por usar mi programa! (: ',font=('Arial',20))
        break
    if evento == 'Guardar gasto':
        monto = values ['MONTO']
        categoria = values ['CATEGORIA']
        fecha = values['FECHA'] if values['FECHA'] else datetime.today().strftime('%Y-%m-%d')
        if not monto or not categoria:
            sg.popup('¡ERROR! Por favor ingrese un monto y una categoria')
            continue
        try:
            float(monto)
        except ValueError:
            sg.popup('¡El monto debe ser un numero valido!')
            continue
        datos = [fecha,categoria,monto]
        datos_csv(archivo_csv, datos, datos_usuario)
        sg.popup('Datos guardados correctamente')

    if evento == "Ver registros":
        if os.path.isfile(archivo_csv):
            with open(archivo_csv, newline='', encoding='utf-8') as f:
                contenido = f.read()
            sg.popup_scrolled("Registros Guardados", contenido, size=(60, 20), font=('Arial', 12))
        else:
            sg.popup_error("No hay registros guardados aún. ):")

    elif evento == "Ver resumen":
        gastos_registrados = leer_gastos_desde_csv(archivo_csv)

        if not gastos_registrados:
            sg.popup_error("No hay gastos registrados para generar un resumen. ):")
            continue

        totales_por_categoria = defaultdict(float)
        total_general = 0.0

        for gasto in gastos_registrados:
            categoria = gasto['Categoria']
            monto = gasto['Monto']

            totales_por_categoria[categoria] += monto
            total_general += monto

        resumen_texto = "--- Resumen de Gastos ---\n\n"
        for categoria, total in totales_por_categoria.items():
            resumen_texto += f"Total {categoria}: ${total:.2f}\n"

        resumen_texto += f"\nTotal General: ${total_general:.2f}"
        sg.popup_scrolled("Resumen de Gastos", resumen_texto, size=(50, 15), font=('Arial', 12))


window.close()

