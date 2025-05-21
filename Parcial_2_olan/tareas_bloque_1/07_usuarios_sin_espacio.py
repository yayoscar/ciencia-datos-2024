usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

for usuario in usuarios:
    usuario_modificado = usuario.replace(" ", "_").capitalize()
    print(usuario_modificado)