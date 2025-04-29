def lista_de_productos():
    productos = ["producto uno", "producto dos", "producto tres", "producto Cuatro"]
    productos_capitalizados = [producto.title().replace(" ", "") for producto in productos]
    for i, producto in enumerate(productos_capitalizados):
        print(f"{i} - {producto}.txt")

lista_de_productos() 