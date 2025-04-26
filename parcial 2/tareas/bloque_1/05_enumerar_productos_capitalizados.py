productos = ["pan", "leche", "manzana", "frijol"]
for i in range(len(productos)):
    nombre = productos[i].capitalize() + ".txt"
    print(i, "-", nombre)