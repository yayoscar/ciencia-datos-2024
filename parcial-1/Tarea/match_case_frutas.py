Fruta= input("Ingresa el nombre de una fruta: ")

match Fruta:
       case "Manzana":
             print("La fruta ingresada es manzana")
       case "Platano":
             print("La fruta ingresada es platano")
       case "Pera":
             print("La fruta ingresada es pera")
       case _:
             print("La fruta no esta registrada o no existe")