def enumerar_productos_capitalizados():
    productos = ["producto uno","producto 2","producto tres","producto cuatro"]
    productos_concapitalize = [producto.title().replace(" ","")for producto in productos]
    for i, producto in enumerate (productos_concapitalize):
        print(f"{i} - {producto}.txt")
enumerar_productos_capitalizados()