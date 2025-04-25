usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_transformados = []
for usuario in usuarios:
    usuario_modificado = usuario.replace(" ", "_").title()
    usuarios_transformados.append(usuario_modificado)
for usuario in usuarios_transformados:
    print(usuario)