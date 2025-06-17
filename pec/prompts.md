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

### Prompt 2
🗨 Pregunta a la IA:
Estoy guardando datos en un archivo .csv, 
pero al abrirlo en Excel se ve todo junto no separado en columnas
como hago para que cada dato aparezca en su propia celda?

📥 Respuesta:
La IA me explicó que, si uso comas para separar los datos, 
Excel a veces no los interpreta bien si está configurado en idioma español
La solución fue usar delimiter=';' al crear el writer de CSV

🧠 Aplicación:
Esto me ayudo a que los datos que guardo, como nombre, precio y total
ya se vean ordenados en columnas cuando abro el archivo .csv con excel
antes se veía todo en una sola celda, ahora cada cosa está en su cuadrito
