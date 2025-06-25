import FreeSimpleGUI as sg
from funciones_main import leer_tareas

layout = [
    [sg.Input(key="entrada_tarea"), sg.Button("Agregar")],
    [sg.Listbox(tareas,size=(50,6))]
]