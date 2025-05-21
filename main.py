
mensaje = "Ingrese una tarea"
todos = []
while True :
        accion_usuario = input("indica que accion quieres realizar agregar/mostrar/listar")
        accion_usuario=accion_usuario.lower()
        accion_usuario=accion_usuario.strip()

        if 'agregar' in accion_usuario:
            todo = accion_usuario[8:]
            todo = f"{todo}\n"

            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)

        elif accion_usuario == 'mostrar' :
            with open ("todos.txt", "r") as archivo
                todos = archivo.readlines()
                print (archivo.read())

