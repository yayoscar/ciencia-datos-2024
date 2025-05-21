mensaje = "ingresa una tarea: "
todos = []
while True:
    accion_usuario=input("ingresa que accion quieres realizar ingrsar/mostrar,listar")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
     case "agregar" :
        todo =input(mensaje)
        todos.append(todo)
     case "mostar" | "listar":
        for elemento in todos:
           elemento = elemento.title()
           print(elemento)     case("salir")  :\             print("No entiendo esa accion")
           print("




