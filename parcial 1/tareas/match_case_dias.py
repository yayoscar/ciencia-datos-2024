print("yo se mucho ingles, ¿no me crees?, te diré el dia de la semana que quieras en inglés")
dia = input("ingresa un dia de la semana como lunes/martes/miercoles/jueves/viernes/sabado/domingo " )
match dia:
    case "lunes":
        print("moonday")
    case "martes":
        print("tuesday")
    case "miercoles":
        print("wednesday")
    case "jueves":
        print("thursday")
    case "viernes":
        print("friday")
    case "sabado":
        print("saturday")
    case "domingo":
        print("sunday")
print(dia.upper())
print("puro duolingo profe :D")