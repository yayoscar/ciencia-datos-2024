usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_modificados = [u.replace(" ", "_").title() for u in usuarios]
print(", ".join(usuarios_modificados))















