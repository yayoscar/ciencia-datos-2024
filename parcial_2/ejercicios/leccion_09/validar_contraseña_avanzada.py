password = input("Ingresa tu contraseña: ")
if len(password) >7:
    print("¡Buena contraseña!")
elif len(password) == 7:
    print("Tu contraseña es buena pero puede ser mejor")
else:
    print("Tu contraseña es débil")