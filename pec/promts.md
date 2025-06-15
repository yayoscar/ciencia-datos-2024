import FreeSimpleGUI as sg

layout = [
    [sg.Text("Meta de ahorro:"), sg.Input(key="META")],
    [sg.Text("Número de semanas:"), sg.Input(key="SEMANAS")],
    [sg.Text("Aporte actual:"), sg.Input(key="APORTE")],
    [sg.Button("Registrar reporte:"), sg.Button(key="ver progreso")]
]

Window = sg.Window("Reto de ahorro personalizado", layout, font=("Arial", 20))
while True:
    evento,valores = Window.read()
    if evento == "Registrar reporte":
        Meta_ahorro=valores["META"]
        Num_semanas=valores["SEMANAS"]
        Aporte_actual=valores["APORTE"]
    if evento == "ver progreso":
        ver_progreso = valores["META", "SEMANAS", "APORTE"]
        if evento:
            datos=("El usuario ha ingresado sus datos")
        else:
            datos=("El usuario aun no completa los datos que se piden.")
        sg.popup(f"{datos}, y ha decidido {evento['Registrar reporte']} o {evento['Ver progreso']}")

    elif evento == sg.WIN_CLOSED:
        break

    Window.close()
Que le falta a mi código


respuesta MetaIA
Faltan algunos pasos importantes en tu código

Para que tu código funcione correctamente y muestre los avances de ahorro, debes realizar los siguientes cambios:

Validar los datos: Asegúrate de que los datos ingresados sean numéricos y no estén vacíos.
Calcular el progreso: Calcula el progreso del ahorro en función de la meta y el aporte actual.
Crear una ventana de progreso: Crea una ventana que muestre los avances de ahorro, incluyendo la meta, el número de semanas, el aporte actual y el progreso.
Corregir la sintaxis: Hay algunos errores de sintaxis en tu código, como evento['Registrar reporte'] y valores["META", "SEMANAS", "APORTE"]






Que es más recomendable usar un if, elif y else o un match case

Respuesta MetaIA
Análisis del Código

Tu código tiene algunos problemas que debes solucionar para que funcione correctamente. A continuación, te presento algunas sugerencias:

1. Validación de datos: Debes validar que los datos ingresados sean numéricos y no estén vacíos.
2. Cálculo de progreso: Debes calcular el progreso del ahorro en función de la meta y el aporte actual.
3. Crear una ventana de progreso: Debes crear una ventana que muestre los avances de ahorro, incluyendo la meta, el número de semanas, el aporte actual y el progreso.

Uso de if, elif y else vs match case

En cuanto a la pregunta sobre qué es más recomendable usar, if, elif y else o match case, depende del contexto y la complejidad de la lógica que estés implementando.

- If, elif y else: Son estructuras de control de flujo que permiten evaluar condiciones y ejecutar código en función de ellas. Son ideales para situaciones simples y complejas.
- Match case: Es una estructura de control de flujo que permite evaluar un valor y ejecutar código en función de él. Es ideal para situaciones en las que se necesita evaluar un valor contra múltiples posibilidades.

En tu caso, podrías usar if, elif y else para evaluar los eventos y ejecutar código en función de ellos. Sin embargo, si tienes muchos eventos que manejar, match case podría ser una buena opción para simplificar el código.