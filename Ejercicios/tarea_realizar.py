mensaje="Tarea a realizar: "
todos = []
while True:
    accion_usuario=input("Indica que accion quieres realizar agregar/mostrar/salir: ")
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
