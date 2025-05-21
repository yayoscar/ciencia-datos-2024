mensaje = "Ingrese una tarea"
todos = []
while True:
    accion_usuario = input("Indica qué acción quieres realizar: agregar/mostrar/editar/: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if 'agregar' in accion_usuario:
        todo = accion_usuario[8:]
        todo = f"{todo}\n"

        with open("todos.txt") as archivo:
            todos = archivo.readlines()