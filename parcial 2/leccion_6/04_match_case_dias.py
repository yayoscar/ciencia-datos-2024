dia = input("ingrese un dia ( en minusculas): ")
match dia:
    case "lunes":
        print("inicio de semana")

    case "miercoles":
        print("Mitad de semana")
    case "sabado"  "domingo":
         print("fin de semana")
    case _:
          print("dia normal")