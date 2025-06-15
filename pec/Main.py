from funciones import *

layout = [
 [sg.Text("Monto inicial:",background_color="#4b5861"), sg.Input(key="INICIAL",background_color="#f6f2e6")],
 [sg.Text("Ahorro mensual:",background_color="#4b5861"), sg.Input(key="MENSUAL",background_color="#f6f2e6")],
 [sg.Text("Meses:",background_color="#4b5861"), sg.Input(key="MESES",background_color="#f6f2e6")],
 [sg.Text("Banco:",background_color="#4b5861"), sg.Combo(["Hey Banco", "NU", "Finsus"], key="BANCO", background_color="#293b3d",text_color="#a8bcba")],
 [sg.Button("Calcular",button_color="#4b5861")],[sg.Button("Cerrar",button_color="#4b5861")]
 ]

banco_valores={
    "Hey Banco": 0.10,
    "NU":0.135,
    "Finsus":0.145
}
archivo = " Simulador de Ahorro en Bancos Digitales.csv"
crear(archivo)
ventana = sg.Window("Ahorro en bancos digitales", layout, icon="JaneDoeChibi.ico", background_color="#839d9e")#Le agregue icono y color

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