import FreeSimpleGUI as sg
import csv

def layout():
    return [
        [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
        [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte","Salud","Ropa","Entretenimiento", "Otros"], key="CATEGORIA")],
        [sg.Text("Fecha (opcional):"), sg.Input(key="FECHA")],
        [sg.Button("Guardar gasto"), sg.Button("Ver resumen"),sg.Button("Salir")]
    ]
def inicializador():
    with open('datos.csv',newline='', mode='w') as data_file:
        fieldnames = ['MONTO', 'CATEGORIA', 'FECHA']
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        data_writer.writeheader()
def guardar(monto,categoria,fecha=None):
    with open('datos.csv',newline='', mode='a') as data_file:
        fieldnames = ['MONTO', 'CATEGORIA', 'FECHA']
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        data_writer.writerow({'MONTO': monto, 'CATEGORIA': categoria, 'FECHA': fecha})
def resumen():
    with open('datos.csv', mode='r') as data_file:
        data_reader = csv.DictReader(data_file)
        comida = 0
        transporte = 0
        salud= 0
        ropa=0
        entretenimiento=0
        otros = 0
        total = 0
        line_count = 0
        for row in data_reader:
            total += float(row['MONTO'])
            if row['CATEGORIA'] == 'Comida':
                comida += float(row['MONTO'])
            elif row['CATEGORIA'] == 'Transporte':
                transporte += float(row['MONTO'])
            elif row['CATEGORIA']=='Salud':
                salud+=float(row['MONTO'])
            elif row['CATEGORIA'] == 'Ropa':
                ropa += float(row['MONTO'])
            elif row['CATEGORIA'] == 'Entretenimiento':
                entretenimiento += float(row['MONTO'])
            elif row['CATEGORIA'] == 'Otros':
                otros += float(row['MONTO'])
        print(f'Total en comida: {comida}')
        print(f'Total en transporte: {transporte}')
        print(f'Total en salud: {salud}')
        print(f'Total en ropa: {ropa}')
        print(f'Total en entretenimiento: {entretenimiento}')
        print(f'Total en otros: {otros}')
        print(f'Total general: {total}')
def abrir():
    ventana = sg.Window("PEC", layout(), font=("Arial", 20))
    while True:
        event, values = ventana.read()
        if event == sg.WIN_CLOSED or event== "Salir":
            sg.popup("Hasta pronto")
            break
        elif event == "Guardar gasto":
            guardar(values['MONTO'], values['CATEGORIA'], values['FECHA'])
            sg.popup("Guardado exitoso!")
            ventana['MONTO']('')
            ventana['CATEGORIA']('')
            ventana['FECHA']('')
        elif event == "Ver resumen":
            resumen()
    ventana.close()