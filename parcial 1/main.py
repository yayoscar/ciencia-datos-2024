mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario= input("indica que accion quieres realizar agregar/mostrar/salir/completar/editar: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar"| "añadir":
            todo = input(mensaje)
            todo = f"{todo}\n"
            archivo = open("todos.txt", "r")
            todos = archivo.readlines()
            archivo.close()
            todos.append(todo)
            archivo = open("todos.txt", "a")
            archivo.writelines(todos)
            archivo.close()
        case "mostrar" | "listar":
            for indice, elemento in enumerate(todos):
                elemento = elemento.title()
                print(f"{indice+1}--{elemento}", end="**")
        case "editar":
            indice = int(input("ingrese el numero de la lista a editar: "))
            nueva_tarea = input("ingresa el nuevo valor de la tarea: ")
            todos[indice-1] = nueva_tarea
        case "completar":
            nueva_tarea = input(("ingrese el nuevo valor para la tarea"))
            indice -= 1
            todos.pop(indice)

        case "salir":
            break
        case _:
            print("no entiendo esta accion")

print("adios")