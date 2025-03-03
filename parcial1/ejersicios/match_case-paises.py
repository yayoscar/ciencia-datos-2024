mensaje = "ingrese un pais"
while True:
    pais=input("indica en que idioma quieres saludar russo/alemania/mexico: ")
    match pais:
        case "russo":
            print("hallo")
        case "italia":
            print("ciao")
        case "mexico":
            print("hola")