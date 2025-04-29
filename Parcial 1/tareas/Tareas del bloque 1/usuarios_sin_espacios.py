def procesar_usuarios():
    usuarios = ["juan perez", "maria lopez", "carlos nuñez"]

    for usuario in usuarios:
        # Capitalizar nombre completo
        usuario_capitalizado = usuario.title()

        # Reemplazar espacios por guiones bajos
        usuario_formateado = usuario_capitalizado.replace(" ", "_")

        # Imprimir resultado
        print(usuario_formateado)

# Ejecutar función
procesar_usuarios()
