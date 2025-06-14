Utilicé ChatGPT como apoyo para comprender mejor lo que se requiiere del proyecto, poder entender la estructura de carpetas y archivos, y asegurarme de que cumplo con las instrucciones del proyecto

Daniela Chin. solo quiero que me epliques que haré.

Chat.gpt: ¡Perfecto! Aquí va una explicación clara y paso a paso de lo que vas a hacer en tu proyecto (Proyecto 3: Calculadora de Gastos Hormiga), para que sepas exactamente qué debes programar y cómo organizarlo:

🎯 ¿Qué es este proyecto?
Vas a crear un programa con interfaz gráfica (usando FreeSimpleGUI) que le ayude al usuario a calcular cuánto dinero podría ahorrar si deja de gastar en cosas pequeñas (como café, cigarros, refrescos, etc.) que compra con frecuencia.

🧩 ¿Qué hará tu programa?
Pedir al usuario los siguientes datos:

Nombre del gasto (ej. “Café”)

Precio por unidad (ej. $35)

Veces por semana que lo consume (ej. 3 veces)

Tiempo en meses que quiere calcular (ej. 6 meses)


Mostrar el resultado en pantalla con sg.popup()

Ejemplo: “Podrías ahorrar $2,520 si evitas este gasto durante 6 meses.”

Guardar los datos en un archivo datos.csv:

Cada vez que alguien usa el programa, se guardará:

nombre del gasto, precio, veces por semana, meses, y ahorro total

🧱 ¿Cómo lo vas a organizar?
Vas a dividir el programa en dos archivos principales:

Archivo	Contenido
main.py	Interfaz gráfica, botones, inputs y llamada a las funciones
funciones.py	Funciones que hacen los cálculos y guardan los datos en el CSV

También tendrás:

datos.csv → donde se guardan los resultados.

prompts.md → para documentar que usaste ChatGPT para guiarte.

🛠️ Herramientas que vas a usar
FreeSimpleGUI para hacer la ventana, botones, cajas de texto, etc.

Funciones de Python para organizar tu código (def calcular_ahorro(...))

CSV para guardar los resultados (usando with open(..., "a"))
