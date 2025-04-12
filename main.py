mensaje = "Ingresa una tarea: "
todos = []
while True:
    accion_usuario=input("Indica que accion quieres realizar mostrar, agregar o salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            for elemento in todos:
                elemento = elemento.title()
            print(elemento)
        case "salir":
            break
        case _:
            print("no entiendo esa accion")
print("Adios")kkdhiqeio hooeqwodwohqej

