import FreeSimpleGUI as sg
from funciones import guardar_gasto, resumen

sg.theme("DarkPurple7")

layout = [
    [sg.Text("Monto del gasto:"), sg.Input(key='monto')],
    [sg.Text("Categoría:"), sg.Combo(['Comida',"Transporte (o gasolina","Impuestos","Colegiatura (gastos de escuela)","Hogar","Ropa","Videojuegos", 'Otros'], key='categoria')],
    [sg.Text("Fecha (opcional, año-mes-dia):"), sg.Input(key='fecha')],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen"), sg.Button("Salir")],
    [sg.Output(size=(60, 10))]
]

window = sg.Window("Registro de Gastos", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Salir"):
        break

    elif event == "Guardar gasto":
        try:
            monto = float(values['monto'])
            categoria = values['categoria']
            fecha = values['fecha'] or None

            if not categoria:
                print(" Selecciona una categoría.")
                continue

            guardar_gasto(monto, categoria, fecha)
            print(" Gasto guardado corectamente.")
        except ValueError:
            print(" Monto inválido. Debe ser un número.")

    elif event == "Ver resumen":
        resumen, total = resumen()
        print(" RESUMEN DE GASTOS")
        for cat, val in resumen.items():
            print(f"  {cat}: ${val:.2f}")
        print(f"  TOTAL GENRAL: ${total:.2f}")

window.close()