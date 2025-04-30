mensaje = "ingresa un tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion deseas realizar agregar/mostrar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
          case "agregar":
              todo = input(mensaje)
              todos.append(todo)
          case "mostrar" | "listar":
              for elemnto in todos:
                print(elemnto)
          case "salir":
              break
          case _:
              print("no entiendo esa accion")