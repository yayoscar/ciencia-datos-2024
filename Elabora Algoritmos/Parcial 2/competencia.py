jurado1 = input("Calificación del primer jurado (Xo no X): ")
jurado2 = input("Calificación del segundo jurado (X o no X): ")
jurado3 = input("Calificación del tercer jurado (X o no X): ")

if jurado1 == "X" and jurado2 == "X" and jurado3 == "X":
    print("El participante queda eliminado.")
else:
    print("El participante no queda eliminado.")