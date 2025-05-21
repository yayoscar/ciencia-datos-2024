productos = ["pan", "leche", "huevo", "arroz"]
for i in range(len(productos)):
    nombre = productos[i].capitalize() + ".txt"
    print(i, "-", nombre)