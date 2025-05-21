edad = int(input("Introduce tu edad "))
vive_en_mexico = input("¿Vives en México? ")
if edad > 18 or edad < 60 and vive_en_mexico == "si":
    print("Eres Mexicano")
else:
    print("Hola")