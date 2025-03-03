mensaje=input("Escribe tu mensaje: ")
match mensaje:
    case "hola" | "hello" | "hi" :
        print("Buenos días")
    case "adios" | "bye" | "chao" :
        print("hasta luego")
    case "" :
        print("No es un mensaje")
