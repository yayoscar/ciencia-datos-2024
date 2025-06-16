### Prompt 1
🗨 Pregunta a la IA:
quiero poner esto en un código:
elif event == sg.WIN_CLOSED:  
    break
pero no me funciona, por que?

📥 Respuesta:
la IA me dijo que para que eso funcione bien, 
la condición de cerrar la ventana debe ir antes de cualquier codigo que use values
porque cuando la ventana se cierra ,
values puede estar vacío o con datos inválidos,
y si se intenta usar esos valores antes de hacer el break, te va a tirar error.

🧠 Aplicación:
Me ayudo a entender la estructura para evitar errores al cerrar la ventana, entonces cambie esto:
elif event == sg.WIN_CLOSED:  
    break
por esto y lo coloque en la linea correcta:
 if event == sg.WIN_CLOSED:
            break
