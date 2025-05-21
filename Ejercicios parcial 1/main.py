mensaje = "ingrese una tarea"
todos = []
while True:
    accion_usuario = input("indique la accion que quieras realizar agregar/mostrar:")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
match accion_usuario:
    case "agregar":
        todo =input(mensaje)
        todos.append(todo)
    case "mostrar" | "listar"
         for elemento in todos:
             print(elemento)
        case"salir":
             break
        case_:
        print("no entiendo esta accion")

