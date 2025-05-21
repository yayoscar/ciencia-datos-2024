pais=input("Ingrese su pais")
match pais:
     case "México" | "mexico" | "Mexico" | "méxico":
         print("Que pex")
     case "Italia" | "italia":
         print("Ciao")
     case "Alemania" | "alemania":
         print ("Hallo")
     case "_":
         print("Pais no reconocido, favor de ingresar un país valido")