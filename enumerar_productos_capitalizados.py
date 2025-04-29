productos = ["producto uno", "producto dos", "producto tres"]  # Example list

for i, producto in enumerate(productos):
    capitalizado = producto.title().replace(" ", "") # Capitalize and remove spaces
    print(f"{i} - {capitalizado}.txt")