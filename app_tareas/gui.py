import FreeSimpleGUI as sg
from funciones import funciones_main as fm
tareas = fm.leer_tareas()

botones = [
    [sg.Push(),sg.Button("Editar") ],[sg.Push(),sg.Button("Completar")],[sg.Push(),sg.Button("Salir")]
]

layout = [
    [sg.Input(key="tarea"), sg.Push(),sg.Button("Agregar Tarea")],
    [sg.Text("Lista De Tareas")],
    [sg.Listbox(tareas, size=(38,10), key="lista"), sg.Push(),sg.Column(botones)]
]
ventana = sg.Window("App Tareas", layout, font=("Bahnschrift", 18))

while True:
    evento, valores = ventana.read()
    if evento == sg.WIN_CLOSED or evento == "Salir":
        break

    elif evento == "Agregar Tarea":
        tarea = valores["tarea"]
        if tarea=="":
            sg.popup("Ingrese un valor en la casilla de arriba para agregar")
            continue
        tarea = f"{tarea}\n"
        tareas.append(tarea)
        fm.guardar_tareas(tareas)
        ventana["lista"].update(tareas)
        ventana["tarea"].update("")

    elif evento == "Editar":
        try:
            tarea = valores["tarea"]
            if tarea=="":
                sg.popup("Ingrese un valor en la casilla de arriba para editar")
                continue
            tarea = f"{tarea}\n"
            tarea_seleccionada = valores["lista"][0]
            indice = tareas.index(tarea_seleccionada)
            tareas[indice]= tarea
            fm.guardar_tareas(tareas)
            ventana["lista"].update(tareas)
            ventana["tarea"].update("")
        except IndexError:
            sg.popup("Seleccione una tarea existente para editar")

    elif evento == "Completar":
        try:
            tarea_seleccionada = valores["lista"][0]
            tareas.remove(tarea_seleccionada)
            fm.guardar_tareas(tareas)
            ventana["lista"].update(tareas)
        except IndexError:
            sg.popup("Seleccione una tarea existente para completar")

ventana.close()