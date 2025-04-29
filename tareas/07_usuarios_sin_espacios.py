usuarios = ["juan perez", "maria lopez", "calos ramirez", "ana martinez", "luis fernandez"]
usuarios_formateados = []
for nombre in usuarios:
    nombre_capitalizados =nombre.title().replace("", "")
    usuarios_formateados.append(nombre_capitalizados)
print(",".join(usuarios_formateados))