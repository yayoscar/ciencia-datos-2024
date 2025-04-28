usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

for usuario in usuarios:
    print(("_" if c == " " else c.upper() if i == 0 or usuario[i-1] == " " else c for i, c in enumerate(usuario)))