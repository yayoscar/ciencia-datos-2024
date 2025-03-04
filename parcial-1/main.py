mensaje = "ingrese un mensaje: "
todos = []
while True:
    accion_usuario =input("indica que accion desea hacer agregar/mostrar/salir: ")
    accion_usuario=accion_usuario.strip()
    accion_usuario=accion_usuario.lower()
    match accion_usuario :
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            for elementos in todos:
                elementos=elementos.title()
                print (elementos)
        case "salir":
            print("nos vemos :(")
            break




