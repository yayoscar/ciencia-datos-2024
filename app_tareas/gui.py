import FreeSimpleGUI as sg
from app_tareas import funciones_main

tareas = funciones_main.leer_tareas()

layout = [
    [sg.Input(key="entrada_tarea"), sg.Button("Agregar")],
    [sg.Listbox(tareas,size=(50,6),key="lista_tareas"),sg.Column(
        [
            [sg.Button("Editar")],
            [sg.Button("Completar")],
            [sg.Button("Salir")]
        ]
    )]
]


window = sg.Window("App Tareas",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    print(evento)
    print(valores)
    if evento==sg.WIN_CLOSED or evento=="Salir":
        break
    elif evento=="Agregar":
        #Obtenemos el valor del Input entrada_tarea
        tarea=valores["entrada_tarea"]
        #Agregamos el salto de linea para el archivo de texto
        tarea = f"{tarea}\n"

        #Obtenemos las tareas del archivo todos.txt a una lista
        todos = funciones_main.leer_tareas()

        #Agregamos la tarea a la lista
        todos.append(tarea)

        #Actualizamos el archivo todos.txt con la lista y la nueva tarea
        funciones_main.guardar_tareas(todos)

        #Actualizamos el Listbox con las tareas actualizadas
        window['lista_tareas'].update(todos)
    elif evento=="Editar":
        tarea=valores["entrada_tarea"]
        tarea = f"{tarea}\n"
        todos = funciones_main.leer_tareas()

        tarea_seleccionada=valores["lista_tareas"][0]
        indice=todos.index(tarea_seleccionada)
        todos[indice]=tarea
        funciones_main.guardar_tareas(todos)
        window['lista_tareas'].update(todos)
    elif evento=="Completar":
        todos = funciones_main.leer_tareas()
        tarea_seleccionada = valores["lista_tareas"][0]
        todos.remove(tarea_seleccionada)
        funciones_main.guardar_tareas(todos)
        window['lista_tareas'].update(todos)

window.close()

