
usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

usuarios_2 = []

for usuario in usuarios:
    usuario_con_guion = usuario.replace(" ", "_")
    partes = usuario_con_guion.split("_")
    partes_capitalizadas = [parte.capitalize() for parte in partes]
    usuario_final = "_".join(partes_capitalizadas)
    usuarios_2.append(usuario_final)

print(", ".join(usuarios_2))
