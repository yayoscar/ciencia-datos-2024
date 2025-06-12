
# Función el cual crea el archivo CSV donde se guardarán los resultados
def crear_csv():

    with open("datos.csv", "w", encoding="utf-8") as f:
        f.write("Producto,Cantidad,Precio tienda 1,Precio tienda 2,Tienda recomendada,Total,Ahorro\n")


# Esta función compara los precios entre dos tiendas y decide cuál es mejor
def comparar(producto, p1, p2, cantidad):

    # Calcula el total por tienda
    total1 = p1 * cantidad
    total2 = p2 * cantidad

    # Para poder compara el total y decidir cual es la opcion mas barata
    if total1 < total2:
        mejor = "Tienda 1"
        ahorro = total2 - total1
        total = total1

    elif total2 < total1:
        mejor = "Tienda 2"
        ahorro = total| - total2
        total = total2
    else:
        mejor = "Ambas tiendas"
        ahorro = 0
        total = total1
        # Formatea el mensaje que se mostrará al usuario
    resultado = (
        f" Mi recomendacion es : {mejor} \n Con la cantidad de: ${total:.2f}\n"
        f" Vas a ahorrar: ${ahorro:.2f}"
    )

    # Para guardar en la fila con los datos en el CSV
    fila_csv = f"{producto},{cantidad},{p1},{p2},{mejor},{total:.2f},{ahorro:.2f}"

    return resultado, fila_csv
