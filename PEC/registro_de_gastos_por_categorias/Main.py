from PEC.registro_de_gastos_por_categorias.funciones import crear_añadir_al_archivo, boton_resumen, ventana
import FreeSimpleGUI as sg

ventana=ventana()
while True:
        event,values=ventana.read()
        if event== "Guardar gasto":
            crear_añadir_al_archivo(values)
            ventana["MONTO"].update("")
            ventana["CATEGORIA"].update("")
            ventana["FECHA"].update("")
        elif event== "Ver resumen":
                boton_resumen()
        elif event==sg.WIN_CLOSED or event =="cerrar":
            break
ventana.Close()



