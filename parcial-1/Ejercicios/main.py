mensaje = "Introdusca una tarea: "
todos = []
while True:
    accion_usuario=input("Indica que accion quieres realizar agregar/mostrar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
         case "agregar":
             todo = input(mensaje)
             todos.append(todo)
         case "mostrar" | "listar":
             for elemento in todos:
                 elemto = elemento.title()
                 print(elemento)
         case "salir":
             break
         case _:
             print("No entiendo esa accion")

print("Adios")