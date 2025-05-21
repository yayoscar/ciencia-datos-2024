mensaje = "ingresa un tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion deseas realizar agregar/mostrar/editar/completar: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    if accion_usuario.startswith("agregar"):
              todo = accion_usuario[8:]
              todo = f"{todo
          case "mostrar" | "listar":
              for elemnto in todos:
                print(elemnto)
          case "salir":
              break
          case _:

              print("no entiendo esa accion")
