
import FreeSimpleGUI as sg

layout = [
    [sg.Input(key='n1')],
    [sg.Input(key='n2')],
    [sg.Button("Sumar"), sg.Button("Restar"), sg.Button("Multiplicar"), sg.Button("Dividir"),
    sg.Button("Cerrar")],
    [sg.Text("Resultado", key="respuesta")]
]

ventana = sg.Window("Ejercicio 3: Calculadora simple",layout, font=("Arial",10))

while True:
    event, values=ventana.read()
    valor1 = int(values['n1'])
    valor2 = int(values['n2'])
    if event=="Sumar":
        suma=valor1+valor2
        ventana["respuesta"].update(f"El resultado de la suma es: {suma}")
    elif event=="Restar":
        restar=valor1-valor2
        ventana["respuesta"].update(f"El resultado de la resta es: {restar}")
    elif event=="Multiplicar":
        multi=valor1*valor2
        ventana["respuesta"].update(f"El resultado de la multiplicacion es: {multi}")
    elif event=="Dividir":
        divicion=valor1/valor2
        ventana["respuesta"].update(f"El resultado de la divicion es: {divicion}")
    elif event=="Cerrar" or event== "sg.WIN_CLOSED":
        break
ventana.close()