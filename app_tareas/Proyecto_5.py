import FreeSimpleGUI as sg
import csv

layout = [
    [sg.Text("Nombre del producto:"), sg.Input(key="PRODUCTO")],
    [sg.Text("Precio en tienda 1:"), sg.Input(key="P1")],
    [sg.Text("Precio en tienda 2:"), sg.Input(key="P2")],
    [sg.Text("Precio en tienda 3:"), sg.Input(key="P3")],
    [sg.Text("Cantidad a comprar:"), sg.Input(key="CANTIDAD")],
    [sg.Button("Comparar precios")]
]
window= sg.Window("Formulario simple", layout, font=('Baoli TC',20))
while True:
    event, values= window.read()
    if event=='Comparar precios':
        nombre=values['PRODUCTO']
        p1=int(values['P1'])
        p2=int(values['P2'])
        p3=int(values['P3'])
        cantidad=int(values['CANTIDAD'])
        tiendas=[p1,p2,p3]
        bara=min(tiendas)*cantidad
        cara=max(tiendas)*cantidad
        diferencia=cara-bara

        with open('comparacion.csv','w',newline='') as archivo_csv:
            pepa_pig=csv.writer(archivo_csv)
            pepa_pig.writerow(['PRODUCTO','TIENDA 1','TIENDA 2','TIENDA 3','CANTIDAD','DIFERENCIA'])
            pepa_pig.writerow([nombre,p1,p2,p3,cantidad,diferencia])

        sg.popup(f"Hola!,el precio mas barato y mas caro es: ", bara,cara,"y la diferencia es: ",diferencia)

    elif event== sg.WIN_CLOSED:
        break
window.close()
