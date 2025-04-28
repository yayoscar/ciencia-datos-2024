from operator import truediv

mensaje = ("Ingrese una tarea")
tdos = []
while True:
    accion_usuario = input("Indica que accion quieres realizar agregar/mostrar/editar/compartir/")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
        case "agregar"|"añadir":
            todo = input(mensaje)
            todo.append(todo)
            archivo = open("todo.txt", "w")
            archivo.writelines()
         case "mostar"| "listar":
             for indice,elemento in enumerate(todos):
                 elemento = elemento.tittle()
                 print((f"{indice+1}--{elemento}"))
         case "Editar":
             indice = int(input("Ingrese el número de la lista a editar: "))
             nueva_tarea = int("Ingrese el nuevo valor para la tarea: ")
             todos[indice+1] = nueva_tarea
        case "completar":
            indice = int(input("Ingrese el número de la lista a completar: ")











