import FreeSimpleGUI as sg
from funciones import registrar_aporte, calcular_progreso, cargar_datos_ahorro, borrar_todos_los_datos
sg.theme('TealMono')

ICON_SAVE = '💾'
ICON_PROGRESS = '📊'
ICON_MONEY = '💰'
ICON_CALENDAR = '📅'
ICON_TARGET = '🎯'
ICON_WARNING = '⚠️'
ICON_CHECK = '✅'
ICON_SAD = '😞'
ICON_DELETE = '🗑️'
layout = [
    [sg.Text(f"{ICON_TARGET} Meta de Ahorro deseada:", font=("Arial", 16)),
     sg.Input(key="META", size=(20, 1), font=("Arial", 16))],
    [sg.Text(f"{ICON_CALENDAR} Periodo (Semanas/Meses):", font=("Arial", 16)),
     sg.Input(key="SEMANAS", size=(20, 1), font=("Arial", 16))],
    [sg.Text(f"{ICON_MONEY} Aporte de ahora:", font=("Arial", 16)),
     sg.Input(key="APORTE", size=(20, 1), font=("Arial", 16))],
    [sg.HSeparator()],  # Línea divisoria para separar los inputs de los botones
    [sg.Button(f"{ICON_SAVE} Registrar Aporte", key="GUARDAR", font=("Arial", 16), button_color=('white', 'green')),
     sg.Button(f"{ICON_PROGRESS} Ver Progreso", key="PROGRESO", font=("Arial", 16), button_color=('white', 'blue')),
     sg.Button(f"{ICON_DELETE} Reiniciar Ahorro", key="BORRAR_TODO", font=("Arial", 16),
               button_color=('white', 'darkred'))],  # Nuevo botón para borrar
    [sg.Text("¡tu puedes solo tienes que cumplir!", font=("Arial", 14), justification='center', expand_x=True,
             relief=sg.RELIEF_SUNKEN,
             background_color='lightblue')],
    [sg.Image(sg.EMOJI_BASE64_COOL, pad=((0, 0), (10, 0)))]
]

window = sg.Window("Ahorra a conciencia ✨", layout, font=("Arial", 20), resizable=False,
                   element_justification='center')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "GUARDAR":
        meta_str = values["META"].strip()
        semanas_str = values["SEMANAS"].strip()
        aporte_str = values["APORTE"].strip()
        if not meta_str or not semanas_str or not aporte_str:
            sg.popup_error(f"{ICON_WARNING} ¡Ups! Te faltan datos.",
                           "Por favor, llena todos los campos para registrar tu aporte.\n",
                           font=("Arial", 14))
        else:
            try:
                float(meta_str)
                int(semanas_str)
                float(aporte_str)
                if registrar_aporte(meta_str, semanas_str, aporte_str):
                    sg.popup_ok(f"{ICON_CHECK} ¡Eso! Continúa así, ¡lo lograrás aún mejor!",
                                "¡Aporte ya guardadito! Ten en mente este sueño, ¡cada centavo lo vale! 💪\n",
                                font=("Arial", 14))
                    window["META"].update('')
                    window["SEMANAS"].update('')
                    window["APORTE"].update('')
                else:
                    sg.popup_error(f"{ICON_WARNING} Error con tus datos",
                                   "Checa que meta, semanas y aporte sean números válidos.\n",
                                   font=("Arial", 14))
            except ValueError:
                # Captura errores si la conversión a número falla
                sg.popup_error(f"{ICON_WARNING} Error de formato",
                               "Favor de ingresar solo números para meta, semanas y aporte.\n",
                               font=("Arial", 14))
    elif event == "PROGRESO":
        datos_actuales = cargar_datos_ahorro()
        if not datos_actuales["aportes_registrados"]:
            sg.popup(f"{ICON_SAD} Sin Datos",
                     "¡Lo siento! Todavía no hay ningún aporte guardado.\n"
                     "¡Comienza a registrar para ver tu progreso!\n",
                     font=("Arial", 14))
        else:
            progreso = calcular_progreso()
            mensaje_ahorrado = "¡Vamos, continua! Ya lograste:" if progreso["ahorrado"] < progreso[
                "meta"] else "¡Lo lograste! ¡Finalmente conseguiste tu meta!"
            mensaje_falta = "¡Ya mero se llega! Solo falta:" if progreso[
                                                                    "falta"] > 0 else "¡Bien! No te falta nada, ¡has superado una meta más en tu vida!"

            color_ahorrado = 'green' if progreso["ahorrado"] >= progreso["meta"] else 'darkorange'
            color_falta = 'darkred' if progreso["falta"] > 0 else 'darkgreen'

            ritmo_color = 'green'
            if "Necesitas acelerar" in progreso["ritmo_mensaje"]:
                ritmo_color = 'red'
            elif "Define" in progreso["ritmo_mensaje"]:
                ritmo_color = 'gray'

            progreso_layout = [
                [sg.Text("✨ ¡Tu Progreso en tu Ahorro! ✨", font=("Arial", 20, "bold"), text_color='purple',
                         justification='center', expand_x=True)],
                [sg.HSeparator()],
                [sg.Text(f"{ICON_TARGET} Meta en general:", font=("Arial", 16)),
                 sg.Text(f"${progreso['meta']:.2f}", font=("Arial", 16, "bold"), text_color='blue')],
                [sg.HSeparator()],
                [sg.Text(f"{ICON_MONEY} {mensaje_ahorrado}", font=("Arial", 16)),
                 sg.Text(f"${progreso['ahorrado']:.2f}", font=("Arial", 16, "bold"), text_color=color_ahorrado)],
                [sg.Text(f"   (Llevas el {progreso['porcentaje']:.2f}% de tu meta)", font=("Arial", 12, "italic"),
                         text_color='gray')],
                [sg.HSeparator()],
                [sg.Text(f"⏳ {mensaje_falta}", font=("Arial", 16)),
                 sg.Text(f"${progreso['falta']:.2f}", font=("Arial", 16, "bold"), text_color=color_falta)],
                [sg.HSeparator()],
                [sg.Text(f"🚀 Como vaz en ahorro:", font=("Arial", 16)),
                 sg.Text(progreso["ritmo_mensaje"], font=("Arial", 16, "bold"), text_color=ritmo_color)],
                [sg.HSeparator()],
                [sg.Text("¡Continua, en el futuro tendras mas metas de ahorros! 🎉", font=("Arial", 14),
                         text_color='darkblue', justification='center', expand_x=True)],
                [sg.Button("¡Entendido!", font=("Arial", 16), button_color=('white', 'darkgreen'), expand_x=True)]
                # Botón para cerrar la ventana de progreso
            ]

            progreso_window = sg.Window("Detalle de Progreso", progreso_layout, modal=True, grab_anywhere=True,
                                        finalize=True)

            while True:
                prog_event, _ = progreso_window.read()
                if prog_event == sg.WIN_CLOSED or prog_event == "¡Entendido!":
                    break
            progreso_window.close()

    elif event == "BORRAR_TODO":
        confirmar = sg.popup_yes_no(f"{ICON_WARNING} ¡Cuidado, eh! ¡Esto es serio!",
                                    "¿De verdad quieres borrar TODO tu historial de ahorro?\n"
                                    "¡Esto no se puede deshacer y empezarías desde cero!\n\n"
                                    "¿Estás 100% seguro de esta decisión?",
                                    font=("Arial", 14),
                                    title="¡ALERTA MÁXIMA!")

        if confirmar == 'Yes':
            if borrar_todos_los_datos():
                sg.popup_ok(f"{ICON_CHECK} ¡Listo!",
                            "¡Historial de ahorro borrado! Ahora puedes empezar de cero.\n"
                            "¡El camino del ahorro te espera de nuevo! 🎉",
                            font=("Arial", 14))
                window["META"].update('')
                window["SEMANAS"].update('')
                window["APORTE"].update('')
            else:
                sg.popup_ok(f"{ICON_SAD} ¡Ups!",
                            "Parece que no había nada que borrar.\n"
                            "¡Tu archivo de datos ya estaba vacío o no existía!",
                            font=("Arial", 14))
        else:
            sg.popup_ok("¡Uff! Menos mal",
                        "¡Sabia decisión! Tu historial de ahorro está a salvo.\n",
                        font=("Arial", 14))

window.close()