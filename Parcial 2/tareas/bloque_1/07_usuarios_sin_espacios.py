usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_sin_espacios = [usuario.replace(" ", "_").title() for usuario in usuarios]
print(", ".join(usuarios_sin_espacios))