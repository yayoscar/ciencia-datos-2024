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
        salud = 0
        ropa = 0
        entretenimiento = 0
        otros = 0
        total = 0
        for row in data_reader:
            monto = float(row['MONTO'])
            total += monto
            categoria = row['CATEGORIA']
            if categoria == 'Comida':
                comida += monto
            elif categoria == 'Transporte':
                transporte += monto
            elif categoria == 'Salud':
                salud += monto
            elif categoria == 'Ropa':
                ropa += monto
            elif categoria == 'Entretenimiento':
                entretenimiento += monto
            elif categoria == 'Otros':
                otros += monto
    encabezado = ['Categoría', 'Total']
    data = [
        ['Comida', f'{comida:.2f}'],
        ['Transporte', f'{transporte:.2f}'],
        ['Salud', f'{salud:.2f}'],
        ['Ropa', f'{ropa:.2f}'],
        ['Entretenimiento', f'{entretenimiento:.2f}'],
        ['Otros', f'{otros:.2f}'],
        ['Total General', f'{total:.2f}']
    ]
    layout = [
        [sg.Table(values=data,
                  headings=encabezado,
                  auto_size_columns=True,
                  justification='center',
                  num_rows=min(len(data), 10))],
        [sg.Button('Cerrar')]
    ]
    window = sg.Window('Resumen de gastos', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Cerrar'):
            break
    window.close()
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