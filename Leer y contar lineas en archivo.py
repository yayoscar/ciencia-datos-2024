try:
    with open("parrafo.txt", "w") as f:
        f.write("This is the first line.\n")
        f.write("This is the second line.\n")
        f.write("This is the third line.\n")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

try:
    with open("parrafo.txt", "r") as f:
        lines = f.readlines()
        line_count = len(lines)
        print(f"El archivo tiene {line_count} líneas")
except FileNotFoundError:
    print("El archivo parrafo.txt no se encontró.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")