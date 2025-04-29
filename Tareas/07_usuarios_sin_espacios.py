
usuarios = ["juan perez", "maria lopez", "ana gomez", "luis fernandez"]
usuarios_modificados = [usuario.replace(' ', '_').title() for usuario in usuarios]
print(', '.join(usuarios_modificados))
