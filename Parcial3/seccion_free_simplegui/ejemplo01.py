import FreeSimpleGUI as sg

layout = [
    [sg.Text("Hola mundo."),sg.Button("Cerrar")],
    [sg.Input(key="NOMBRE")], # Si fuera el normal, sería nombre=input()
    [sg.Checkbox("Aceptar términos", key="t_y_c")],
    [sg.Radio("Opción A","GRUPO1", key="a"), sg.Radio("Opción B", "GRUPO2")],
    [sg.Combo(["Rojo", "Verde", "Azul"], key='COLOR')],
    [sg.Slider(range=(1,100), orientation='h', key='SLIDER')],
    [sg.Multiline(size=(30,5), key="COMENTARIO")]
]
#Creando la ventana
window = sg.Window("Ejemplo01 - Mi primera GUI", layout,font=('Arial',20))

#Monstrar la ventana una vez.
window.read()
window.close()


