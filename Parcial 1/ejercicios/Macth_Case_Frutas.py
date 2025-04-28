# Match_Case-Frutas
fruta = input("Ingresa el nombre de una futa: ")
match fruta:

     case "Manzana":
         print("Manzana")
     case "Naranja":
         print("Naranja")
     case "Sandía":
         print("Sandía")
     case "Pera":
         print("Pera")
     case "Limón":
         print("Limón")
     case "Melón" | "Fruta grande":
         print("Melón", "Fruta grande")
     case "Durazno" | "Fruta de piel lisa":
         print("Durazno", "Fruta de piel lisa")
     case "Mandarina" | "Fruta cítrica":
         print("Mandarina", "Fruta cítrica")
     case "Fresa":
            print("categoría desconocida")








