def leer_tareas (ruta_archivo):
        with open(ruta_archivo, "r") as archivo_local:
            todos_local = archivo_local.readlines()
            return todos_local


def guardar_tareas(ruta_archivos,todos_arg):
    with open(ruta_archivos, "w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Ingresa que accion quieres realizar agregar/mostrar/editar/salir ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}\n"

        todos = leer_tareas("todos.txt")

        todos.append(todo)

        guardar_tareas("todos.txt",todos)


    elif accion_usuario.startswith("mostar"):
        todos = leer_tareas()



