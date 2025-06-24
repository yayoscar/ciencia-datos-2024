import FreeSimpleGUI as sg
from funciones import funciones_main
tareas = funciones_main.leer_tareas()


layout = [
    [sg.Input(key="entrada_tarea", text_color="purple", background_color="white"),sg.Button("Agregar Tarea", button_color=("purple"))],
    [sg.Listbox(tareas,size=(30, 6),key="lista_tareas",text_color="purple",background_color="white"),sg.Column(
        [
            [sg.Button("Editar Tarea",button_color=("purple"))],
            [sg.Button("Completar Tarea", button_color=("purple"))],
            [sg.Button("Salir", button_color=("purple"))]
        ],background_color="pink",vertical_alignment="top", pad=(150,0)
    )]
]

window = sg.Window("App tareas",layout,font=("Arial",15),background_color="pink")

while True:
    evento,valores = window.read()
    print(evento)
    print(valores)
    if evento == sg.WIN_CLOSED or evento=="Salir":
        break
    elif evento=="Agregar":
        #Obtenemos el valor del Input entrada_tarea
        tarea = valores["entrada_tarea"]
        #el salto de linea para el archivo de texto
        tarea = f"{tarea}\n"


        todos = funciones_main.leer_tareas()
        todos.append(tarea)

        funciones_main.guardar_tareas(todos)

        #Se actualiza el List box con las tareas actualizados
        window['lista_tareas'].update(todos)
    elif evento=="Editar":
        tarea = valores["entrada_tarea"]
        tarea = f"{tarea}\n"
        todos = funciones_main.leer_tareas()

        tarea_seleccionada = valores["lista_tareas"][0]
        indice = todos.index(tarea_seleccionada)
        todos[indice]=tarea
        funciones_main.guardar_tareas(todos)
        window["lista_tareas"].update(todos)
    elif evento=="Completar":
        todos = funciones_main.leer_tareas()
        tarea_seleccionada = valores["entrada_tarea"][0]
        todos.remove(tarea_seleccionada)
        window['lista_tareas'].update(todos)


window.close()
