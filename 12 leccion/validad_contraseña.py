def fuerza(contraseña):
    if len(contraseña) > 7:
        print("¡Es buena la contraseña!")
    elif len(contraseña) == 7:
        print("¡Tu contraseña es buena pero es débil!")
    else:
        print("¡Contraseña débil!")
