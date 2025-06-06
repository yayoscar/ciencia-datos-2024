import FreeSimpleGUI as sg
def menu():
    print('menu')


layout = [
    [sg.Text("Hola mundo", background_color='#8EC6B5', text_color='#180D6F' )],
    [sg.Button('Cerrar')],
    [sg.Input(key= 'nombre')],
    [sg.Checkbox("Aceptar términos", key= "t_y_c",  background_color='#8EC6B5', text_color='#180D6F' )],
    [sg.Radio('Opción a', 'Grupo1', key = 'a',  background_color='#8EC6B5', text_color='#180D6F' ), sg.Radio('Opción B', 'Grupo1', key = 'b',  background_color='#8EC6B5', text_color='#180D6F' )],
    [sg.Combo(['Verde', 'Rojo', 'Azul', 'Amarillo'], key= 'Color')],
    [sg.Slider(range=(1,100), orientation='h', key= 'Slider',  background_color='#8EC6B5', text_color='#180D6F' )],
    [sg.Multiline(size= (10, 2), key = 'comentario')],
    [sg.Canvas(size=(800,10), background_color='#180D6F')]
]

window = sg.Window("Ejemplo01 - Mi primer GUI", layout, font=("Arial", 20), background_color='#8EC6B5')

lectura = window.read()
print(lectura)
window.close()

