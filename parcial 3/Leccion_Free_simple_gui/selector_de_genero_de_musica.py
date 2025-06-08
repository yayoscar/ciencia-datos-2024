import FreeSimpleGUI as sg

layaut = [
[sg.Radio("Rock", "G", key="Rock"),
 sg.Radio("Pop", "G", key="Pop"),
 sg.Radio("Jazz", "G", key="Jazz"),
 sg.Radio("Clásica", "G", key="Clásica")],
    [sg.Button("confirmar")]]

sg.Window("Género Musical", layaut).read(close=True)
