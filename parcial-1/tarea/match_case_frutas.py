fruta = input("piensa en una fruta:")
match fruta:
    case "manzana","durazno","pera":
      print("la",fruta,"es una fruta de piel lisa")
    case "naranja","limon","mandarina":
        print("la",fruta,"es una fruta citrica")
    case "sandia","melon":
        print("la",fruta,"es uan fruta grande")
