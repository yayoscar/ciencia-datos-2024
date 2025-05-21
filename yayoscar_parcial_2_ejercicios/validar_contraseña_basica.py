password = input("ingresa una nueva contraseña:")
if len(password) > 7:
    print("¡buena contraseña!")
if len(password) <= 7:
    print("tu contraseña no sirve osea es debil.")