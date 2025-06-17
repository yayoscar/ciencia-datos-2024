from funciones import *
ventana=ventana()

banco_valores = {
    "Hey Banco": 0.10,
    "NU": 0.135,
    "Finsus": 0.145
}
archivo = "Simulador de Ahorro en Bancos Digitales.csv"
crear(archivo)
while True:
    event, values=ventana.read()
    if event=="Cerrar" or event==sg.WIN_CLOSED:
        break
    elif event=="Calcular":
        monto_inicial=int(values["INICIAL"])
        ahorro_mensual=int(values["MENSUAL"])
        meses=int(values["MESES"])
        tasa_mensual=banco_valores[values["BANCO"]]/12
        valor_final=calculo(tasa_mensual,meses,ahorro_mensual,monto_inicial)
        datos=[monto_inicial,ahorro_mensual,meses,values["BANCO"], valor_final]
        guardar_datos(archivo,datos)
        sg.popup("Calculo realizado y guardado con exito")

ventana.close()

#Profe el resultado de el ejemplo de Monto inicial: 3000, Mensual: 1000, Meses: 6, Banco: NU (13.5% anual), Tendrías $9,750 al finalizar los 6 meses, el resultado nunca fue 9750, el resultado de este ejemplo es el que esta en el archivo csv