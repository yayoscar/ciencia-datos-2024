mensaje = "ingresa una tarea"
todos = []
while True:
    accion_usuario=input("indica que accion quieres realizar agregar/mostrar,listar/salir:")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
           todo = input(mensaje)
           todos.append(todo)
        case "mostrar" :
            for elemento in todos:
                elemento = elemento.title()
                print(elemento)
            print(todos)
        case "salir":
            break
        case _:
            print("no entiendo esa accion")

print("adios")

