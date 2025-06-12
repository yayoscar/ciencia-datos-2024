import csv
import FreeSimpleGUI as pipshas

adriana_salte = [
    [pipshas.Text("Monto del gasto: "), pipshas.Input(key="monto")],
    [pipshas.Text("Categoría: "), pipshas.Combo(["Comida","Transporte (o gasolina)","Impuestos","Colegiatura (gastos de escuela)","Hogar","Gastos médicos","Ropa","Videojuegos","Otro"], key="Categoria")],
    [pipshas.Text("Fecha: "),pipshas.Input(key="Fecha")],
    [pipshas.Multiline(size=(40, 10), key='output')],
    [pipshas.Button("Save"), pipshas.Button("Show"), pipshas.Button("Close")]

]
XP = pipshas.Window("CONTROL DE GASTOS", adriana_salte, font=("Helvetica", 14))
while True:
    event, values = XP.read()
    if event == 'Close' or pipshas.WIN_CLOSED:
        break
    elif event == "Save":
        with open('info.csv', 'a', newline='') as csvfile:
            info_global= ['Monto del gasto', 'Categoría', 'Fecha',]
            writer = csv.DictWriter(csvfile, fieldnames= info_global)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'Monto del gasto': values['monto'],
                'Categoría':values['Categoria'],
                'Fecha':values['Fecha']

            })
        pipshas.popup("Información guardada exitosamente!!!!!")
    elif event == "Show":
        Monto= values['monto']
        Categoria= values['Categoria']
        Fecha= values['Fecha']

        output= f"Monto: {Monto}\nCategoría: {Categoria}\nFecha: {Fecha}"
        XP['output'].update(output)

XP.close()
