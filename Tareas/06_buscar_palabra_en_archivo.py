palabra_buscada = input("Introduce la palabra que quieres buscar: ").strip()
# 3. Leer el archivo y contar las apariciones
with open('texto.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    contador = contenido.split().count(palabra_buscada)
# 4. Imprimir el resultado
print(f"La palabra aparece {contador} veces.")
