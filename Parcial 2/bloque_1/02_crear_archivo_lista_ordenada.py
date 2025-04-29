def números_flotantes():
    números = [9.8, 4.76, 12.3, 3.14, 8.5]
    números_orden = [3.14, 4.76, 8.5, 9.8, 12.3]
    números.sort()
    with open("orden.txt", "w") as archivo:
        archivo.write(", ".join(f"{i+1}- {n}" for i, n in enumerate(números)))

números_flotantes()
