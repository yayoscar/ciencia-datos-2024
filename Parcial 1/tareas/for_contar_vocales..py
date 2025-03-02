
nombres = ["hola", "mundo", "python", "programacion"]


for nombre in nombres:

    num_vocales = (
            nombre.count("a") + nombre.count("e") + nombre.count("i") +
            nombre.count("o") + nombre.count("u")
    )

    print(f"{nombre} tiene {num_vocales} vocales.")
