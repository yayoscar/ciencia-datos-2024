def usuarios_sin_espacios():
    usuarios = ["juan perez", "maria lopez","carlos nuñez"]
    usuarios_procesados = [usuario.replace(" ", "_").title() for usuario in usuarios]
    print(",".join(usuarios_procesados))
usuarios_sin_espacios()