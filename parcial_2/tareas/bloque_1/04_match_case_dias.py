while True:
 dia = input("Ingrese un dia de la semana correctamente escrito y acentuado totalmente en minúscula: ")
 match dia:
     case "lunes":
         print("Inicio de semana")
         print ()
     case "miércoles":
        print ("Mitad de semana")
        print()
     case "sábado" | "domingo":
         print ("Fin de semana")
         print()
     case "martes" | "jueves":
         print ("Dia normal")
         print()
     case get:
         print ("POR FAVOR, INGRESE ÚNICAMENTE LO SOLICITADO")
         print()