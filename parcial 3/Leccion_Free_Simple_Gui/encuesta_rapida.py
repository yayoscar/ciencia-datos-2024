import FreeSimpleGUI as fsg
layout= [
    [fsg.Checkbox("¿Te gusta Python?")],
    [fsg.Text('¿Qué versión usas?'), fsg.Combo([2.7, 3.6, 3.9, 3.11])],
    [fsg.Text('Comentarios:')],
    [fsg.Multiline(size=(15,5))],
    [fsg.Button('Enviar')]
]
ventana = fsg.Window('encuesta rápida', layout)
ventana.read()
ventana.close()