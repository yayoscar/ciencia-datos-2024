while True:
    print("Mexico , Alemania, Italia")
    accion_usuario= input("Indica de que pais eres:  ")
    match accion_usuario:
        case "Mexico" :
            print("Hola")
        case "Alemania" :
            print("hallo")
        case "Italia" :
            print("Ciao")