usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
usuarios_transformados = [nombre.replace( '',     '_').title() for nombre in usuarios]
resultado =" , ".join(usuarios_transformados)
print(resultado)