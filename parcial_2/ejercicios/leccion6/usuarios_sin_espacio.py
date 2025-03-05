users = ["pirata culiacan", "huesos pepe", "enrique milanon"]
for user in users:
    usuario_modificado = user.replace(" ", "_").capitalize()
    print(usuario_modificado)