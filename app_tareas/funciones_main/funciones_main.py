#funciones_main.py
RUTA = "todos.txt"

def leer_tareas(ruta_archivo=RUTA):
    """Retorna una lista de tareas a partir de una ruta"""
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local

def guardar_tareas(todos_arg,ruta_archivo=RUTA):
    """Guarda en un archivo la lista de tareas"""
    with open(ruta_archivo, "w") as archivo_local:
        archivo_local.writelines(todos_arg)

if _name_ == "_main_":
    print("Hola desde funciones")