mensaje = "ingrese una tarea"
todos = []
accioN_usuario = input("indica que acción quieres realiza o mostrar")
accioN_usuario = accioN_usuario.strip()
accioN_usuario = accioN_usuario.lower()
        match accioN_usuario :
            case "agregar" :
                todo = input(mensaje)
                 todos.append(todo)
                case " mostar"| "listar":
                 for elemento in todos :
                     print(elemento)
                case "salir":
                    break
                case _:
                 print("No entiendo esa accion")

    print("Adios")