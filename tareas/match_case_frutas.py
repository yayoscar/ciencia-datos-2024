fruta = input("ingresa el nombre de una fruta")

match fruta.lower():

     case "manzana"|"pera"|"durazno":
        print("fruta de piel lisa")
     case "naranja"|"limon"|"mandarina":
        print("fruta critica")
     case "sandia"|"melon":
        print("fruta grande")
     case _:
        print("categoria desconocida")




