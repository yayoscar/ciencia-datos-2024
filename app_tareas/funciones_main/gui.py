import FreeSimpleGUI as sg

layout = [
    [sg.Input(key="Entrada"), sg.Button("Agregar")],
    [sg.Listbox(["Tarea", "Tarea2"],size=(50,6),key="Lista_tareas"),sg.colum(  ]