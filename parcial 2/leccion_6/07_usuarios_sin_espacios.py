usuarios = ["juan perez","maria lopez","carlos nuñez"]
for usuario in usuarios:
    usuario_modificado = usuario.replace(" ", "_").title()
    print(usuario_modificado)