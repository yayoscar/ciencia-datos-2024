usuarios = ["juan perez", "maria lopez", "carlos ramirez", "ana martinez", "luis fernandez"]

usuarios_formateados = []
for nombre in usuarios:
    nombre_capitalizado = nombre.title().replace(" ", "_")
    usuarios_formateados.append(nombre_capitalizado)

print(" , ".join(usuarios_formateados))
