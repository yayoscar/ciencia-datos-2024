import

mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que accion quieres realizar agregar/mostrar/editar/")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}"

        todos = funciones_main.leer_tareas()
    