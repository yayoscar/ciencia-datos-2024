Dia= input("Ingresa el dia que quiera combertir en ingles: ")

match Dia:
       case "Lunes" | "lunes":
             print("Monday")
       case "Martes" | "martes":
             print("Tuesday")
       case "Miercoles" | "miercoles":
             print("Wednesday")
       case "Jueves" | "jueves":
             print("Thursday")
       case "Viernes" | "viernes":
             print("Friday")
       case "Sabado" | "sabado":
             print("Saturday")
       case "Domingo" | "domingo":
             print("Sunday")
       case _:
           print("Este dia no existe/This day doesn't exist")