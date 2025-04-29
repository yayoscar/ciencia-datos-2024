usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_transformados = [nombre.replace(__old= "", __new= "_").title() for nombre in usuarios]
resultado =" , ".join(usuarios_transformados)
print(resultado)