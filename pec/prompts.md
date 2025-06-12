La IA que utilicé fue Claude Sonnet 4

# Yo.-Necesito que me expliques, como si fueras un maestro de programación y paso a paso, cómo puedo guardar una fila de dos datos de un archivo de Python a un archivo csv

Te explico paso a paso cómo guardar datos en un archivo CSV desde Python:

## Método 1: Usando el módulo csv (Recomendado)

### Paso 1: Importar el módulo
```python
import csv
```

### Paso 2: Preparar tus datos
```python
# Una fila con dos datos
fila = ['Juan', 25]
# O varios datos si quieres guardar múltiples filas
datos = [
    ['Juan', 25],
    ['María', 30],
    ['Pedro', 28]
]
```

### Paso 3: Escribir al archivo CSV
```python
# Para escribir una sola fila
with open('archivo.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(fila)

# Para escribir múltiples filas
with open('archivo.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)  # Nota: writerows (plural)
```

### Paso 4: Agregar datos a un archivo existente
```python
# Para agregar sin sobrescribir, usa modo 'a' (append)
with open('archivo.csv', 'a', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Ana', 22])
```

## Método 2: Usando pandas (Más potente)

### Paso 1: Instalar e importar pandas
```python
import pandas as pd
```

### Paso 2: Crear y guardar datos
```python
# Crear un DataFrame
datos = {
    'Nombre': ['Juan', 'María'],
    'Edad': [25, 30]
}
df = pd.DataFrame(datos)

# Guardar al CSV
df.to_csv('archivo.csv', index=False)
```

## Ejemplo completo funcional:

```python
import csv

# Datos que quieres guardar
persona = ['Carlos', 35]

# Crear archivo CSV con encabezados
with open('personas.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    # Escribir encabezados
    escritor.writerow(['Nombre', 'Edad'])
    # Escribir datos
    escritor.writerow(persona)

print("Archivo CSV creado exitosamente")
```

## Puntos importantes:

1. **newline=''**: Evita líneas en blanco extras en Windows
2. **encoding='utf-8'**: Maneja caracteres especiales correctamente
3. **Modo 'w'**: Sobrescribe el archivo. Usa 'a' para agregar
4. **with open()**: Se asegura de cerrar el archivo automáticamente

¿Te gustaría que profundice en algún aspecto específico o tienes algún caso particular que necesitas resolver?

# Yo.-Para lo que estoy haciendo tengo que asegurarme que el primer dato sea numérico, paso a paso explícame cómo puedo hacer eso. Son filas de 2 datos

Te explico paso a paso cómo validar que el primer dato sea numérico antes de guardarlo en el CSV:

## Paso 1: Función para verificar si un dato es numérico

```python
def es_numerico(valor):
    """Verifica si un valor es numérico"""
    try:
        float(valor)  # Intenta convertir a número
        return True
    except ValueError:
        return False
```

## Paso 2: Función para validar y limpiar una fila

```python
def validar_fila(fila):
    """Valida que una fila tenga exactamente 2 datos y el primero sea numérico"""
    # Verificar que tenga exactamente 2 elementos
    if len(fila) != 2:
        return False, "La fila debe tener exactamente 2 datos"
    
    # Verificar que el primer dato sea numérico
    if not es_numerico(fila[0]):
        return False, f"El primer dato '{fila[0]}' no es numérico"
    
    # Convertir el primer dato a número (float o int)
    primer_dato = float(fila[0])
    # Si es un entero, lo convertimos a int
    if primer_dato.is_integer():
        primer_dato = int(primer_dato)
    
    # Retornar fila validada
    fila_validada = [primer_dato, fila[1]]
    return True, fila_validada
```

## Paso 3: Función completa para guardar con validación

```python
import csv

def guardar_fila_validada(fila, nombre_archivo):
    """Guarda una fila en CSV después de validarla"""
    
    # Validar la fila
    es_valida, resultado = validar_fila(fila)
    
    if not es_valida:
        print(f"Error: {resultado}")
        return False
    
    # Si es válida, guardar en CSV
    try:
        with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(resultado)
        
        print(f"Fila guardada correctamente: {resultado}")
        return True
        
    except Exception as e:
        print(f"Error al guardar archivo: {e}")
        return False
```

## Paso 4: Ejemplo de uso completo

```python
import csv

def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def validar_fila(fila):
    if len(fila) != 2:
        return False, "La fila debe tener exactamente 2 datos"
    
    if not es_numerico(fila[0]):
        return False, f"El primer dato '{fila[0]}' no es numérico"
    
    primer_dato = float(fila[0])
    if primer_dato.is_integer():
        primer_dato = int(primer_dato)
    
    fila_validada = [primer_dato, fila[1]]
    return True, fila_validada

def guardar_fila_validada(fila, nombre_archivo):
    es_valida, resultado = validar_fila(fila)
    
    if not es_valida:
        print(f"Error: {resultado}")
        return False
    
    try:
        with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(resultado)
        
        print(f"Fila guardada correctamente: {resultado}")
        return True
        
    except Exception as e:
        print(f"Error al guardar archivo: {e}")
        return False

# Ejemplos de uso
datos_prueba = [
    ['25', 'Juan'],      # Válido: '25' se convierte a 25
    ['30.5', 'María'],   # Válido: '30.5' se convierte a 30.5
    ['abc', 'Pedro'],    # Inválido: 'abc' no es numérico
    [42, 'Ana'],         # Válido: ya es numérico
    ['18', 'Luis', 'Extra']  # Inválido: más de 2 datos
]

# Crear archivo con encabezados
with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Numero', 'Nombre'])

# Probar cada fila
for fila in datos_prueba:
    print(f"\nProbando fila: {fila}")
    guardar_fila_validada(fila, 'datos.csv')
```

## Paso 5: Versión más robusta (Opcional)

Si quieres ser más específico sobre el tipo de número:

```python
def validar_numero_especifico(valor, solo_enteros=False):
    """Validación más específica de números"""
    try:
        if solo_enteros:
            int(valor)
            return True, int(valor)
        else:
            numero = float(valor)
            # Si es entero, devolver como int
            if numero.is_integer():
                return True, int(numero)
            return True, numero
    except ValueError:
        return False, None
```

## Resultado esperado:

Al ejecutar el código, verás algo como:
```
Probando fila: ['25', 'Juan']
Fila guardada correctamente: [25, 'Juan']

Probando fila: ['30.5', 'María']
Fila guardada correctamente: [30.5, 'María']

Probando fila: ['abc', 'Pedro']
Error: El primer dato 'abc' no es numérico

Probando fila: [42, 'Ana']
Fila guardada correctamente: [42, 'Ana']
```

¿Te gustaría que ajuste algún aspecto específico de la validación o tienes algún caso particular que necesitas manejar?

# Yo.-Ahora cómo puedo mostrar los datos de un archivo csv en mi interfaz gráfica (usando FreeSimpleGUI) en un archivo .py

Te explico paso a paso cómo mostrar datos CSV en una interfaz gráfica con FreeSimpleGUI:

## Paso 1: Instalar FreeSimpleGUI

```bash
pip install FreeSimpleGUI
```

## Paso 2: Función para leer el archivo CSV

```python
import csv
import FreeSimpleGUI as sg

def leer_csv(nombre_archivo):
    """Lee un archivo CSV y retorna los datos como lista de listas"""
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                datos.append(fila)
        return True, datos
    except FileNotFoundError:
        return False, "Archivo no encontrado"
    except Exception as e:
        return False, f"Error al leer archivo: {e}"
```

## Paso 3: Crear la interfaz básica

```python
def crear_interfaz():
    """Crea la ventana principal"""
    
    # Layout de la ventana
    layout = [
        [sg.Text('Visualizador de datos CSV', font=('Arial', 16))],
        [sg.Button('Cargar CSV'), sg.Button('Actualizar'), sg.Button('Salir')],
        [sg.Table(values=[], headings=['Columna 1', 'Columna 2'], 
                 max_col_width=25, num_rows=10, key='-TABLA-',
                 enable_events=True, justification='center')],
        [sg.Text('', key='-STATUS-')]
    ]
    
    return sg.Window('Visor CSV', layout, resizable=True)
```

## Paso 4: Ejemplo completo funcional

```python
import csv
import FreeSimpleGUI as sg

def leer_csv(nombre_archivo):
    """Lee un archivo CSV y retorna los datos"""
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                datos.append(fila)
        return True, datos
    except FileNotFoundError:
        return False, "Archivo no encontrado"
    except Exception as e:
        return False, f"Error al leer archivo: {e}"

def crear_interfaz():
    """Crea la ventana principal"""
    
    sg.theme('LightBlue2')  # Tema visual
    
    layout = [
        [sg.Text('📊 Visualizador de datos CSV', font=('Arial', 16, 'bold'))],
        [sg.HorizontalSeparator()],
        
        # Botones de control
        [sg.Button('📁 Seleccionar CSV', key='-CARGAR-'), 
         sg.Button('🔄 Actualizar', key='-ACTUALIZAR-'), 
         sg.Button('❌ Salir', key='-SALIR-')],
        
        # Tabla para mostrar datos
        [sg.Table(values=[], 
                 headings=['Número', 'Descripción'], 
                 max_col_width=30, 
                 num_rows=15, 
                 key='-TABLA-',
                 enable_events=True, 
                 justification='left',
                 alternating_row_color='lightgray',
                 header_background_color='navy',
                 header_text_color='white')],
        
        # Barra de estado
        [sg.Text('Listo para cargar archivo...', key='-STATUS-', 
                text_color='blue', font=('Arial', 10))]
    ]
    
    return sg.Window('Visor de Datos CSV', layout, resizable=True, size=(600, 500))

def main():
    """Función principal"""
    
    ventana = crear_interfaz()
    archivo_actual = None
    
    while True:
        evento, valores = ventana.read()
        
        # Cerrar ventana
        if evento in (sg.WIN_CLOSED, '-SALIR-'):
            break
        
        # Cargar archivo CSV
        elif evento == '-CARGAR-':
            archivo = sg.popup_get_file('Seleccionar archivo CSV',
                                      file_types=(("CSV Files", "*.csv"), ("All Files", "*.*")))
            
            if archivo:
                exito, datos = leer_csv(archivo)
                
                if exito:
                    if datos:
                        # Actualizar tabla (sin encabezados si la primera fila son datos)
                        ventana['-TABLA-'].update(values=datos)
                        ventana['-STATUS-'].update(f'✅ Cargado: {len(datos)} filas desde {archivo}')
                        archivo_actual = archivo
                    else:
                        ventana['-STATUS-'].update('⚠️ El archivo está vacío')
                else:
                    sg.popup_error(f'Error al cargar archivo:\n{datos}')
                    ventana['-STATUS-'].update('❌ Error al cargar archivo')
        
        # Actualizar datos
        elif evento == '-ACTUALIZAR-':
            if archivo_actual:
                exito, datos = leer_csv(archivo_actual)
                if exito:
                    ventana['-TABLA-'].update(values=datos)
                    ventana['-STATUS-'].update(f'🔄 Actualizado: {len(datos)} filas')
                else:
                    sg.popup_error(f'Error al actualizar:\n{datos}')
            else:
                sg.popup('Primero selecciona un archivo CSV')
        
        # Selección en tabla
        elif evento == '-TABLA-':
            if valores['-TABLA-']:
                fila_seleccionada = valores['-TABLA-'][0]
                ventana['-STATUS-'].update(f'Fila seleccionada: {fila_seleccionada + 1}')
    
    ventana.close()

if __name__ == '__main__':
    main()
```

## Paso 5: Versión con encabezados automáticos

Si tu CSV tiene encabezados en la primera fila:

```python
def leer_csv_con_headers(nombre_archivo):
    """Lee CSV separando encabezados de datos"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)  # Primera fila como encabezados
            datos = list(lector)        # Resto como datos
        return True, encabezados, datos
    except Exception as e:
        return False, [], f"Error: {e}"

# En la función main(), cambiar la parte de cargar:
elif evento == '-CARGAR-':
    archivo = sg.popup_get_file('Seleccionar archivo CSV',
                              file_types=(("CSV Files", "*.csv"),))
    
    if archivo:
        exito, headers, datos = leer_csv_con_headers(archivo)
        
        if exito:
            # Actualizar encabezados y datos
            ventana['-TABLA-'].update(values=datos)
            # Si quieres cambiar los encabezados dinámicamente:
            # ventana['-TABLA-'].update(values=datos, headings=headers)
            ventana['-STATUS-'].update(f'✅ Cargado: {len(datos)} filas')
            archivo_actual = archivo
```

## Paso 6: Agregar funcionalidades extra

```python
# Agregar al layout:
[sg.Button('💾 Exportar Selección'), sg.Button('🗑️ Limpiar Tabla')],

# En el bucle principal:
elif evento == '💾 Exportar Selección':
    if valores['-TABLA-']:
        # Código para exportar filas seleccionadas
        pass
        
elif evento == '🗑️ Limpiar Tabla':
    ventana['-TABLA-'].update(values=[])
    ventana['-STATUS-'].update('Tabla limpiada')
```

## Resultado:

Al ejecutar obtendrás una ventana con:
- Botón para seleccionar archivo CSV
- Tabla que muestra los datos en columnas
- Barra de estado con información
- Funcionalidad de actualización

¿Te gustaría que agregue alguna funcionalidad específica como filtros, edición de datos, o búsqueda?

# Yo.-Cómo puedo hacer que la lista de listas (del método 1) se muestre en forma de tabla? Explícame paso a paso

Te explico paso a paso cómo convertir una lista de listas en una tabla visual usando FreeSimpleGUI:

## Paso 1: Entender la estructura de datos

```python
# Tu lista de listas se ve así:
datos = [
    [1, 'Juan'],
    [2, 'María'],
    [3, 'Pedro'],
    [4.5, 'Ana']
]
```

## Paso 2: Usar el elemento Table de FreeSimpleGUI

```python
import FreeSimpleGUI as sg

# Configuración básica del elemento Table
tabla = sg.Table(
    values=datos,                    # Tu lista de listas aquí
    headings=['Número', 'Nombre'],   # Títulos de las columnas
    max_col_width=25,               # Ancho máximo de columnas
    num_rows=10,                    # Número de filas visibles
    key='-TABLA-'                   # Identificador único
)
```

## Paso 3: Ejemplo básico completo

```python
import FreeSimpleGUI as sg

def mostrar_tabla_basica():
    # Tus datos (lista de listas)
    datos = [
        [1, 'Juan'],
        [2, 'María'],
        [3, 'Pedro'],
        [4.5, 'Ana'],
        [5, 'Carlos']
    ]
    
    # Definir el layout
    layout = [
        [sg.Text('Mi Tabla de Datos', font=('Arial', 16))],
        [sg.Table(values=datos, 
                 headings=['Número', 'Nombre'],
                 max_col_width=25,
                 num_rows=10,
                 key='-TABLA-',
                 justification='center')],
        [sg.Button('Cerrar')]
    ]
    
    # Crear ventana
    ventana = sg.Window('Tabla Simple', layout)
    
    # Bucle de eventos
    while True:
        evento, valores = ventana.read()
        if evento in (sg.WIN_CLOSED, 'Cerrar'):
            break
    
    ventana.close()

# Ejecutar
mostrar_tabla_basica()
```

## Paso 4: Versión más personalizada

```python
import FreeSimpleGUI as sg

def crear_tabla_personalizada(datos, encabezados):
    """Crea una tabla personalizada con más opciones"""
    
    sg.theme('LightBlue2')
    
    layout = [
        [sg.Text('📊 Tabla de Datos', font=('Arial', 16, 'bold'))],
        [sg.HorizontalSeparator()],
        
        # Tabla con más opciones de personalización
        [sg.Table(values=datos,
                 headings=encabezados,
                 max_col_width=30,
                 num_rows=15,
                 key='-TABLA-',
                 enable_events=True,           # Habilita eventos de clic
                 justification='left',         # Alineación del texto
                 alternating_row_color='lightgray',  # Color alternado
                 header_background_color='navy',     # Color del encabezado
                 header_text_color='white',          # Color texto encabezado
                 selected_row_colors=('white', 'blue'),  # Color fila seleccionada
                 enable_click_events=True,     # Eventos de clic
                 right_click_selects=True)],   # Clic derecho selecciona
        
        [sg.Text('Selecciona una fila para ver información', key='-INFO-')],
        [sg.Button('Cerrar')]
    ]
    
    return sg.Window('Tabla Personalizada', layout, resizable=True)

def main():
    # Tus datos
    datos = [
        [1, 'Juan Pérez'],
        [2.5, 'María González'],
        [3, 'Pedro Martínez'],
        [4.8, 'Ana López'],
        [5, 'Carlos Rodríguez'],
        [6.2, 'Sofía Hernández']
    ]
    
    encabezados = ['ID', 'Nombre Completo']
    
    ventana = crear_tabla_personalizada(datos, encabezados)
    
    while True:
        evento, valores = ventana.read()
        
        if evento in (sg.WIN_CLOSED, 'Cerrar'):
            break
        
        # Manejar selección de fila
        elif evento == '-TABLA-':
            if valores['-TABLA-']:  # Si hay fila seleccionada
                fila_index = valores['-TABLA-'][0]
                fila_datos = datos[fila_index]
                ventana['-INFO-'].update(f'Seleccionado: ID={fila_datos[0]}, Nombre={fila_datos[1]}')
    
    ventana.close()

if __name__ == '__main__':
    main()
```

## Paso 5: Conectar con tu función de leer CSV

```python
import csv
import FreeSimpleGUI as sg

def leer_csv_a_lista(nombre_archivo):
    """Lee CSV y retorna lista de listas"""
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                # Convertir primer elemento a número si es posible
                try:
                    fila[0] = float(fila[0])
                    if fila[0].is_integer():
                        fila[0] = int(fila[0])
                except:
                    pass  # Mantener como string si no es número
                datos.append(fila)
        return True, datos
    except Exception as e:
        return False, str(e)

def mostrar_csv_como_tabla():
    """Muestra CSV como tabla en GUI"""
    
    sg.theme('DefaultNoMoreNagging')
    
    layout = [
        [sg.Text('Visualizador CSV como Tabla', font=('Arial', 16))],
        [sg.Button('📁 Cargar CSV'), sg.Button('🔄 Actualizar'), sg.Button('❌ Cerrar')],
        [sg.Table(values=[],
                 headings=['Número', 'Dato'],
                 max_col_width=35,
                 num_rows=12,
                 key='-TABLA-',
                 enable_events=True,
                 justification='left',
                 alternating_row_color='#f0f0f0',
                 header_background_color='#4472c4',
                 header_text_color='white',
                 font=('Courier', 11))],
        [sg.Text('Total de filas: 0', key='-CONTADOR-')],
        [sg.Text('Listo para cargar archivo...', key='-STATUS-')]
    ]
    
    ventana = sg.Window('CSV → Tabla', layout, resizable=True)
    archivo_actual = None
    
    while True:
        evento, valores = ventana.read()
        
        if evento in (sg.WIN_CLOSED, '❌ Cerrar'):
            break
        
        elif evento == '📁 Cargar CSV':
            archivo = sg.popup_get_file('Seleccionar CSV', 
                                      file_types=(("CSV", "*.csv"),))
            if archivo:
                exito, datos = leer_csv_a_lista(archivo)
                if exito:
                    ventana['-TABLA-'].update(values=datos)
                    ventana['-CONTADOR-'].update(f'Total de filas: {len(datos)}')
                    ventana['-STATUS-'].update(f'✅ Cargado: {archivo}')
                    archivo_actual = archivo
                else:
                    sg.popup_error(f'Error: {datos}')
        
        elif evento == '🔄 Actualizar' and archivo_actual:
            exito, datos = leer_csv_a_lista(archivo_actual)
            if exito:
                ventana['-TABLA-'].update(values=datos)
                ventana['-CONTADOR-'].update(f'Total de filas: {len(datos)}')
                ventana['-STATUS-'].update('🔄 Actualizado')
        
        elif evento == '-TABLA-' and valores['-TABLA-']:
            indice = valores['-TABLA-'][0]
            ventana['-STATUS-'].update(f'Fila {indice + 1} seleccionada')
    
    ventana.close()

# Ejecutar
mostrar_csv_como_tabla()
```

## Paso 6: Personalización avanzada de la tabla

```python
# Opciones adicionales para el elemento Table:

tabla_avanzada = sg.Table(
    values=datos,
    headings=['Col1', 'Col2'],
    
    # Apariencia
    font=('Helvetica', 12),           # Fuente
    background_color='white',         # Color de fondo
    text_color='black',              # Color del texto
    
    # Comportamiento
    auto_size_columns=True,          # Ajuste automático de columnas
    def_col_width=20,               # Ancho por defecto
    select_mode=sg.TABLE_SELECT_MODE_BROWSE,  # Modo de selección
    
    # Barras de desplazamiento
    vertical_scroll_only=False,      # Solo scroll vertical
    hide_vertical_scroll=False,      # Ocultar scroll vertical
    
    # Eventos
    bind_return_key=True,           # Enter selecciona fila
    tooltip='Haz clic para seleccionar una fila'
)
```

## Resultado final:

Tu lista de listas se mostrará como una tabla profesional con:
- Encabezados personalizables
- Filas seleccionables
- Colores alternados
- Información de estado
- Capacidad de actualización

¿Te gustaría que agregue alguna funcionalidad específica como ordenamiento, filtros o edición de celdas?

# Yo.-Cómo puedo hacer que automáticamente (sin que el usuario lo ingrese) añada la fecha de el día (Día/Mes/Año) como otro dato en cada fila en el archivo csv? Es decir, cuando el usuario ingrese el dinero y la categoría, cómo hago que se añada la fecha? Explícame paso a paso.
Te explico paso a paso cómo añadir automáticamente la fecha actual a cada fila del CSV:

## Paso 1: Importar el módulo datetime

```python
import csv
from datetime import datetime
```

## Paso 2: Función para obtener la fecha actual

```python
def obtener_fecha_actual():
    """Obtiene la fecha actual en formato DD/MM/YYYY"""
    fecha_hoy = datetime.now()
    return fecha_hoy.strftime("%d/%m/%Y")

# Ejemplo de uso:
print(obtener_fecha_actual())  # Salida: 11/06/2025
```

## Paso 3: Modificar tu función de validación para incluir fecha

```python
import csv
from datetime import datetime

def es_numerico(valor):
    """Verifica si un valor es numérico"""
    try:
        float(valor)
        return True
    except ValueError:
        return False

def obtener_fecha_actual():
    """Obtiene la fecha actual en formato DD/MM/YYYY"""
    return datetime.now().strftime("%d/%m/%Y")

def validar_y_agregar_fecha(dinero, categoria):
    """Valida el dinero y agrega la fecha automáticamente"""
    
    # Validar que el dinero sea numérico
    if not es_numerico(dinero):
        return False, f"El dinero '{dinero}' no es numérico"
    
    # Convertir dinero a float o int
    dinero_numerico = float(dinero)
    if dinero_numerico.is_integer():
        dinero_numerico = int(dinero_numerico)
    
    # Obtener fecha actual
    fecha_actual = obtener_fecha_actual()
    
    # Crear fila completa: [dinero, categoria, fecha]
    fila_completa = [dinero_numerico, categoria, fecha_actual]
    
    return True, fila_completa
```

## Paso 4: Función para guardar con fecha automática

```python
def guardar_gasto_con_fecha(dinero, categoria, archivo_csv):
    """Guarda un gasto con fecha automática al CSV"""
    
    # Validar y preparar datos
    es_valido, resultado = validar_y_agregar_fecha(dinero, categoria)
    
    if not es_valido:
        print(f"Error: {resultado}")
        return False
    
    # Guardar en CSV
    try:
        with open(archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(resultado)
        
        print(f"Gasto guardado: {resultado}")
        return True
        
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False
```

## Paso 5: Ejemplo completo de uso

```python
import csv
from datetime import datetime

def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

def validar_y_agregar_fecha(dinero, categoria):
    if not es_numerico(dinero):
        return False, f"El dinero '{dinero}' no es numérico"
    
    dinero_numerico = float(dinero)
    if dinero_numerico.is_integer():
        dinero_numerico = int(dinero_numerico)
    
    fecha_actual = obtener_fecha_actual()
    fila_completa = [dinero_numerico, categoria, fecha_actual]
    
    return True, fila_completa

def guardar_gasto_con_fecha(dinero, categoria, archivo_csv):
    es_valido, resultado = validar_y_agregar_fecha(dinero, categoria)
    
    if not es_valido:
        print(f"Error: {resultado}")
        return False
    
    try:
        with open(archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(resultado)
        
        print(f"Gasto guardado: {resultado}")
        return True
        
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

def crear_archivo_con_headers(archivo_csv):
    """Crea el archivo CSV con encabezados si no existe"""
    try:
        with open(archivo_csv, 'x', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['Dinero', 'Categoria', 'Fecha'])
        print("Archivo creado con encabezados")
    except FileExistsError:
        print("El archivo ya existe")

# Ejemplo de uso
if __name__ == "__main__":
    archivo = "gastos.csv"
    
    # Crear archivo con encabezados (solo la primera vez)
    crear_archivo_con_headers(archivo)
    
    # Simular entrada de usuario
    gastos_ejemplo = [
        ("250.50", "Comida"),
        ("1000", "Renta"),
        ("50", "Transporte"),
        ("75.25", "Entretenimiento")
    ]
    
    # Guardar cada gasto
    for dinero, categoria in gastos_ejemplo:
        print(f"\nGuardando: {dinero} - {categoria}")
        guardar_gasto_con_fecha(dinero, categoria, archivo)
```

## Paso 6: Integración con FreeSimpleGUI

```python
import csv
import FreeSimpleGUI as sg
from datetime import datetime

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def guardar_gasto_automatico(dinero, categoria, archivo):
    """Guarda gasto con fecha automática"""
    if not es_numerico(dinero):
        return False, "El dinero debe ser numérico"
    
    dinero_num = float(dinero)
    if dinero_num.is_integer():
        dinero_num = int(dinero_num)
    
    fecha = obtener_fecha_actual()
    fila = [dinero_num, categoria, fecha]
    
    try:
        with open(archivo, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fila)
        return True, fila
    except Exception as e:
        return False, str(e)

def crear_interfaz_gastos():
    """Interfaz para registrar gastos"""
    sg.theme('LightBlue2')
    
    layout = [
        [sg.Text('💰 Registro de Gastos', font=('Arial', 16, 'bold'))],
        [sg.HorizontalSeparator()],
        
        [sg.Text('Dinero:'), sg.Input(key='-DINERO-', size=(15, 1))],
        [sg.Text('Categoría:'), sg.Input(key='-CATEGORIA-', size=(20, 1))],
        
        [sg.Button('💾 Guardar Gasto'), sg.Button('📊 Ver Gastos'), sg.Button('❌ Salir')],
        
        [sg.Text('', key='-STATUS-', text_color='blue')],
        [sg.Text(f'Fecha actual: {obtener_fecha_actual()}', font=('Arial', 10), text_color='gray')]
    ]
    
    return sg.Window('Control de Gastos', layout)

def main():
    archivo_gastos = "mis_gastos.csv"
    
    # Crear archivo con headers si no existe
    try:
        with open(archivo_gastos, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Dinero', 'Categoria', 'Fecha'])
    except FileExistsError:
        pass
    
    ventana = crear_interfaz_gastos()
    
    while True:
        evento, valores = ventana.read()
        
        if evento in (sg.WIN_CLOSED, '❌ Salir'):
            break
        
        elif evento == '💾 Guardar Gasto':
            dinero = valores['-DINERO-'].strip()
            categoria = valores['-CATEGORIA-'].strip()
            
            if not dinero or not categoria:
                ventana['-STATUS-'].update('⚠️ Completa todos los campos')
                continue
            
            exito, resultado = guardar_gasto_automatico(dinero, categoria, archivo_gastos)
            
            if exito:
                ventana['-STATUS-'].update(f'✅ Guardado: ${resultado[0]} - {resultado[1]} - {resultado[2]}')
                # Limpiar campos
                ventana['-DINERO-'].update('')
                ventana['-CATEGORIA-'].update('')
            else:
                ventana['-STATUS-'].update(f'❌ Error: {resultado}')
        
        elif evento == '📊 Ver Gastos':
            # Aquí podrías abrir otra ventana para mostrar los gastos
            sg.popup(f'Los gastos están guardados en: {archivo_gastos}')
    
    ventana.close()

if __name__ == '__main__':
    main()
```

## Paso 7: Personalizar formato de fecha (Opcional)

```python
def obtener_fecha_personalizada(formato="dd/mm/yyyy"):
    """Obtiene fecha en diferentes formatos"""
    fecha = datetime.now()
    
    formatos = {
        "dd/mm/yyyy": "%d/%m/%Y",        # 11/06/2025
        "yyyy-mm-dd": "%Y-%m-%d",        # 2025-06-11
        "dd-mm-yyyy": "%d-%m-%Y",        # 11-06-2025
        "mm/dd/yyyy": "%m/%d/%Y",        # 06/11/2025
        "completa": "%d/%m/%Y %H:%M:%S"  # 11/06/2025 14:30:25
    }
    
    return fecha.strftime(formatos.get(formato, "%d/%m/%Y"))

# Ejemplos:
print(obtener_fecha_personalizada("dd/mm/yyyy"))  # 11/06/2025
print(obtener_fecha_personalizada("yyyy-mm-dd"))  # 2025-06-11
print(obtener_fecha_personalizada("completa"))    # 11/06/2025 14:30:25
```

## Resultado en el CSV:

Tu archivo CSV se verá así:
```
Dinero,Categoria,Fecha
250.5,Comida,11/06/2025
1000,Renta,11/06/2025
50,Transporte,11/06/2025
75.25,Entretenimiento,11/06/2025
```

## Puntos clave:

1. **Automático**: La fecha se añade sin intervención del usuario
2. **Formato consistente**: Siempre DD/MM/YYYY
3. **Validación**: Sigue validando el dinero como numérico
4. **Tres columnas**: Dinero, Categoría, Fecha

¿Te gustaría que agregue alguna funcionalidad adicional como hora específica, diferentes formatos de fecha, o validación de categorías?
