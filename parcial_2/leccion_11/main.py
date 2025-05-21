def leer_tareas(ruta_archivo="todos.txt"):
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


def guardar_tareas(todos_arg,ruta_archivo="todos.txt"):
    with open(ruta_archivo, "w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion quieres realizar agregar/mostrar/editar/")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}/n"
