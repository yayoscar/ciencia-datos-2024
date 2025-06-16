# prompts.md

## Fecha: 14/06/2025

### Prompt:
¿Está bien como estoy haciendo mi programa, cómo se usaba popup, podría mejorar algo?

### Respuesta del modelo:
Me respondió que el programa estaba bien estructurado, con los archivos separados correctamente y usando PySimpleGUI para la interfaz, como lo pedía el proyecto.

También me explicó que para mostrar resultados se puede usar `sg.popup()`, por ejemplo:

```python
sg.popup(f"renta final después de {meses} meses: ${resultado}")


