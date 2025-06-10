import FreeSimpleGUI as sg

layout= [
    [sg.Text("Monto del gasto: "), sg.Input(key="MONTO")],
    [sg.Text("Categoria"), sg.Combo(["Comida", "Transporte", "Otros"], key="CATEGORIA")],
    [sg.Text("Fecha (opcional)"), sg.Input(key="FECHA")],
    [sg.Button("Guardar gasto"), sg.Button("Ver resumen")]

]

ventana = sg.Window("Registro de Gastos y Categorias",layout,font=("Comic Sans",20))

ventana.read()
ventana.close()