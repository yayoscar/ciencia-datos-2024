mensaje = input("mensaje: ")
match mensaje:
    case "Hola" | "Hello" | "Hi":
        print ("Buenos días")
    case "Adiós" | "Bye":
        print ("Hasta luego")
    case _:
        print("No es un mensaje válido")

#| pipe: or (o)
#Operadores lógicos:
#True and True = True
#True and False = False
#False and True = False
#False and False = False

#True or True = True
#True or False = True
#False or True = True
#False or False = False