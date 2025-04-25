usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_modificados = [usuario.replace(" ", "_").title() for usuario in usuarios]
print(", ".join(usuarios_modificados))
