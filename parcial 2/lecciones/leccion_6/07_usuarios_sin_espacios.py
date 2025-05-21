usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_formateados = [nombre.title().replace(" ", "_") for nombre in usuarios]
print(", ".join(usuarios_formateados))