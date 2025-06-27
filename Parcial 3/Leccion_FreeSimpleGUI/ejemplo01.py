import FreeSimpleGUI as sg

layout = [
  [sg.Text("Hola Mundo"),sg.Button('Cerrar')],
  [sg.Input(key="Nombre")],
  [sg.Checkbox("Aceptar terminos", key="t_y_c")],
  [sg.Radio("Opcion A","GRUPO1", key="a"), sg.Radio("Opcion B", "GRUPO1",key="b")],
  [sg.Combo(["rojo","verde", "rosa"],key="COLOR")],
  [sg.Slider(range=(1, 100),orientation="h", key="SILDER")],
  [sg.Multiline(size=(30, 5), key="COMENTARIO")]
]

window = sg.Window("Ejemplo01- Mi primer GUI",layout,font=('Algerian',20))

window.read()
window.close()