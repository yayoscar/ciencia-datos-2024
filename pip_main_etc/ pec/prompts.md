🗨 Pregunta a la IA:
¿Como puedo asignarle valores a un combo en FreeSimpleGUI?

� Respuesta:
Claro, te explicaré paso a paso cómo asignar valores a un Combo ya existente en PySimpleGUI utilizando un diccionario.

Paso 1: Crear el Combo

Primero, debes crear el Combo en tu ventana de PySimpleGUI. Puedes hacer esto utilizando el elemento sg.Combo() y especificando las opciones que deseas mostrar en el Combo.
layout = [
    [sg.Combo(["Opción 1", "Opción 2", "Opción 3"], key="-COMBO-")],
    [sg.Button("Obtener valor")]
]
Paso 2: Crear el diccionario

Luego, debes crear un diccionario que asocie valores a cada opción del Combo. El diccionario debe tener las opciones del Combo como claves y los valores que deseas asignar como valores.
valores_diccionario = {
    "Opción 1": 10,
    "Opción 2": 20,
    "Opción 3": 30
}

� Aplicación:
 con esto pude a los bancos que estaban en el combo, asignarle valores, como seria un valor de porcentaje los puse en punto decimal
