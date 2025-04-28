mensaje = "ingresa una tarea: "
todos = []
while True:
    accion_usuario=input("indica que accion quieres realizar salir/mostrar: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            for elemento in todos:
              print(elemento)
        case "salir":
            break
        case _:
            print("no entiendoesa accion")

print("adios")