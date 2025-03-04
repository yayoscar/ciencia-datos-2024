mensaje = "ingrese un mensaje: "
todos = []
while True:
    accion_usuario =input("indica que accion desea hacer agregar/mostrar/editar/completar/salir: ")
    accion_usuario=accion_usuario.strip()
    accion_usuario=accion_usuario.lower()
    match accion_usuario :
        case "agregar"| " añadir":
            todo = input(mensaje)
            todo = f"{todo}\n"
            archivo.close()
            todos.append(todo)
            archivo = open("todos.txt", "r")
            archivo.writelines(todo)
            archivo.close()

        case "mostrar"| "listar":
            for (indice,elemento) in enumerate(todos):
                elemento = elemento.title()
                print (f"{indice+1}--{elemento}",end="")
        case "editar":
          indice = int(input("ingrese el numero de la lista a editar: "))
          nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
          nueva_tarea = f"{nueva_tarea}\n"
          todos[indice-1] = nueva_tarea
          archivo = open("todos.txt", "r")
          archivo.writelines(todos)
          archivo.close()
        case "completar":
            indice = int(input("ingrese el numero de la lista a completar:   "))
            indice -=1
            todos.pop(indice)
            archivo = open("todos.txt", "r")
            archivo.writelines(todos)
            archivo.close()

        case "salir":
            print("nos vemos :(")
            break
        case _:
            print("no entiendo esta accion")







