password = input("Ingresa una nueva contraseña: ")
if len(password) > 7:
    print("!es buena la contraseña¡")
elif len(password):
    print("!tu contraseña es buena pero es debil¡")
if len(password) < 7:
    print("!contraseña debil¡")