nombres = ["juan pérez", "maría lópez", "carlos nuñez"]
for nombre in nombres:
    nombre_capitalizado = nombre.title().replace(" ", "_")
    print(nombre_capitalizado)
