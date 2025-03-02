mensaje = "Ingresa una tarea"
todos =[]
while True:
    accion_usuario=input("indica que accion quieres realizas agregar/mostrar,listar:")
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar"|"listar":
            for elemento in todos:
                elemento=elemento.title()
                print (elemento)
        case  "salir":
            break
        case _:
            print("no entiendo esa accion")

print ("adios")
