mensaje = "Ingresa una tarea:"
todos = []
while True:
    accion_usuario = input("Indica que accion quieres realizar agregar/mostrar,listar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar" | "añadir" :
            todo = input(mensaje)
            todo = f"{todo}\n"
            archivo = open("todos.txt","r")
            todos = archivo.readlines()
            archivo.close()
            todos.append(todo)
            archivo = open("todos.txt","w")
            archivo.writelines(todos)
            archivo.close()
        case "mostrar" | "listar":
            archivo = open("todos.txt","r")
            todos = archivo.readlines()
            archivo.close()
            for indice,elemento in enumerate(todos):
                elemento = elemento.title()
                print(f"{indice+1}--"
                      f"elemento)
            todos.pop(indice)
        case "salir":
            break
        case _:
            print("No entiendo tu mensaje")
print("Adios")
