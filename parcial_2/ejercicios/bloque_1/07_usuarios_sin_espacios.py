usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

usuarios_procesados = []
for usuario in usuarios:
    nombre_capitalizado = usuario.title()
    nombre_con_guiones = nombre_capitalizado.replace(" ", "_")
    usuarios_procesados.append(nombre_con_guiones)

print(", ".join(usuarios_procesados))