nombres = ["juan perez", "maria lopez", "carlos nuñez"]


nombres_formateados = [nombre.replace(" ", "_").title() for nombre in nombres]

print(", ".join(nombres_formateados))