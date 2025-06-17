#funciones del programa
import FreeSimpleGUI as sg
#ventana principal
def ventana():
    layout = [
        [sg.Text("Monto del gasto:"), sg.Input(key="MONTO")],
        [sg.Text("Categoría:"), sg.Combo(["Comida", "Transporte", "ropa","entretenimiento","otro escribalo"],
                                         key="CATEGORIA")],
        [sg.Text("Fecha (D/M/A):"), sg.Input(key="FECHA")],
        [sg.Button("Guardar gasto"), sg.Button("Ver resumen"),sg.Button("cerrar")]
    ]
    window=sg.Window("registro de gastos y categorias",layout,font=("Arial",25))
    return window

#funciones para el boton guardar datos
def crear_añadir_al_archivo(values):

  try:
      monto = values["MONTO"]
      categoria = values["CATEGORIA"]
      fecha = values["FECHA"]
      if str(values["MONTO"]).isnumeric()==False:
          sg.popup_error("el monto debe ser un numero entero o flotante")
      if  str(values["CATEGORIA"]).isnumeric()==True:
          sg.popup_error("la categoria no puede ser un numero")
      if  values["MONTO"]=="" or  values["CATEGORIA"]=="":
          sg.popup_error("error haci bien feo:\n","el cuadro de categoria y monto son obligatorios")
      else:

          if values["FECHA"]=="":
              formato_final =categoria,monto
              formato_a_archivo = ",".join(formato_final)

              with open("datos.csv", "a") as archivo:
                  impresion_final = f"{formato_a_archivo}\n"
                  archivo.writelines(impresion_final)
          else:

                    dia,mes,año=fecha.split("/")
                    fecha=año,mes,dia
                    formato_fecha="-".join(fecha)
                    formato_final=formato_fecha,categoria,monto
                    formato_a_archivo=",".join(formato_final)

                    with open("datos.csv","a") as archivo:
                        impresion_final=f"{formato_a_archivo}\n"
                        archivo.write(impresion_final)
                    return
  except AttributeError:
    sg.popup("ingrese un numero valido")

#funcion para el boton resumen
def boton_resumen():
    with open("datos.csv", "r") as archivo:
        archivo=archivo.readlines()
        total_por_categoria = {}
        monto_total=0
        resumen_completo="\n"
        try:
            for linea in archivo:
              linea = linea.split(",")

              if len(linea)==3:
                    fecha,categoria,monto=linea
                    monto= float(monto)
                    resumen_completo += (f"{categoria}: ${monto:},{fecha} \n")
              elif len(linea) == 2:
                    categoria, monto = linea
                    monto = float(monto)
                    resumen_completo += f"{categoria}: ${monto:} \n"


              monto_total += monto
              total_por_categoria[categoria] = total_por_categoria.get(categoria, 0.0) + monto
            resumen_completo += "\n-------------- Total por Categorías ------------------\n"

            for categoria, total in total_por_categoria.items():
                     resumen_completo += f"{categoria}: ${total:} \n"
            resumen_completo += f"\n               Monto Total Gastado:\n ${monto_total:} "

            sg.popup_scrolled(
                "resumen",
                "------------Resumen completo----------------",
                 resumen_completo,
                 size=(40,34),
                font=("Arial",15))
        except ValueError :
                sg.popup_error("ingrese otro dato")
                return



#total_por_categoria.get

