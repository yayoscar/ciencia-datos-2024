usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_modificados = []
for usuarioss in usuarios:
    usuarios_sin_espacios = usuarioss.replace(" ", "_")
    usuarios_capitalizados = usuarios_sin_espacios.title()
    usuarios_modificados.append(usuarios_capitalizados)
print(", ".join(usuarios_modificados))