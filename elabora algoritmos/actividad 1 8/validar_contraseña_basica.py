password = input("Ingresa una nueva contraseña: ")
if len(password) > 7:
    print("!es buena la contraseña¡")
if len(password) < 7:
    print("contraseña debil")