
usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_formateados = [usuario.title().replace(" ", "_") for usuario in usuarios]

print(" , ".join(usuarios_formateados))
