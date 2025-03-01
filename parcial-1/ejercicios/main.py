mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario=input("indica que accion quieres realizar agregar/mostrar,listar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar" | "listar":
            for elemento in todos:
                print(elemento)
        case "salir":
            break
        case _:
            print("no entiendo esa accion")

print("Adios")