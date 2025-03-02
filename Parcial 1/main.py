mensaje = "Ingrese una tarea"
todos = []
while True :
        accion_usuario = input("indica que accion quieres realizar agregar/mostrar/listar")
        accion_usuario=accion_usuario.strip()
        match accion_usuario:
            case "agregar" | "Agregar":
                todo= input(mensaje)
                todos.append(todo)
            case "mostrar":
                for elemento in todos :
                    elemento = elemento.title()
                    print(elemento)
            case "salir":
                break
            case _:
                print("No entiendo esta acción")

print ("Adios")
