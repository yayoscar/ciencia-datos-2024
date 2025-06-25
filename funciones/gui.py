import FreeSimpleGUI

layout = [
    [FreeSimpleGUI.input(key="entrada_tarea"),sg.Button("Agregar")],
    [sg.Listbox(["Tarea", "Tarea2"],size=(50,6),key="lista_tareas"), sg.Column(
        [
            [sg.Button("Editar")],
            [sg.Button("Completar")],
            [sg.Button("Salir")]
    )]
]

window = sg.Window("App tareas",layout,font="Arial",)

while True:
    evento,valores = window.read()
    if evento==sg.WIN_CLOSED or evento == "Salir":
        break

window.close()