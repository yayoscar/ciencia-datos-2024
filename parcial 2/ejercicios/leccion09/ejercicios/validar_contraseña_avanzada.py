password= input("ingresa nueva contraseña: ")
largo= len(password)
if len(password)>7:
    print("buena contraseña!")
elif largo == 7:
    print("la contraseña esta bien pero es debil")
else:
    print("tu contraseña es mala:(")