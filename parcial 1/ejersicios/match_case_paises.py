mensaje = "ingresa un pais"
while True:
    pais=input("ingresa el idioma en el que quieres ser saludado  mexico/italia/alemania ")
    match pais:
        case "mexico":
            print("hola")
        case "italia":
            print("ciao")
        case "alemania":
            print("hallo")
        case "salir":
            break

