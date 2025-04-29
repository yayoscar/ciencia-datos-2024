usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

for usuario in usuarios:
    procesado = usuario.replace(" ", "_").title()
    print(f'"{procesado}", ', end="")

print()