from typing import Dict

#La problematica trata de que una persona comun sin informacion de cierto animal quiere saber como se encuetra en la base de datos de animales en peligro de extincion
ESPECIES_MEXICO: Dict[str, str] = {
    "Jaguar": "Peligro de extinción",
    "Vaquita Marina": "En peligro crítico",
    "Ajolote": "En peligro",
    "Tortuga Caguama": "Vulnerable",
    "Lobo Mexicano": "En peligro",
    "Puma": "Preocupación menor",
    "Zopilote Rey": "Preocupación menor",
    "Tapir Centroamericano": "En peligro",
    "Guacamaya Roja": "Amenazada",
}

def normalizar_especie(nombre: str) -> str:
    """introduce el nombre de la especie para su búsqueda."""
    return ' '.join(palabra.capitalize() for palabra in nombre.strip().split())

def obtener_estado_conservacion(especie: str, base_datos: Dict[str, str]) -> str:
    """Devuelve el estado de conservación de una especie si existe."""
    especie_formateada = normalizar_especie(especie)
    return base_datos.get(especie_formateada, None)

def mostrar_menu():
    print("=" * 50)
    print(" Clasificador de Animales en Peligro - México ".center(50, "-"))
    print("=" * 50)
    print("Escribe el nombre de la especie o 'salir' para terminar.\n")

def clasificar_especies():
    """Función principal para interactuar con el usuario."""
    mostrar_menu()

    while True:
        especie = input("🔎 Buscar especie: ").strip()
        if not especie:
            print("⚠️  Por favor, escribe un nombre válido.\n")
            continue

        if especie.lower() == "salir":
            print("\n✅ Gracias por usar el clasificador. ¡Hasta pronto!")
            break

        estado = obtener_estado_conservacion(especie, ESPECIES_MEXICO)
        if estado:
            print(f"🟢 La especie '{normalizar_especie(especie)}' está clasificada como: {estado}\n")
        else:
            print(f"🔴La especie '{especie}' no se encuentra en la base de datos.\n")

if __name__ == "__main__":
    clasificar_especies()