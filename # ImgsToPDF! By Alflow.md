# ImgsToPDF! By Alflow

Una aplicación de escritorio simple y elegante para convertir imágenes a PDF.

## Características

- Interfaz gráfica simple.
- Dos modos de selección:
  - Carpeta completa: convierte todas las imágenes de una carpeta
  - Imágenes sueltas: selecciona imágenes específicas
- Soporta formatos: PNG, JPG, JPEG, TIFF
- Selección flexible del destino del PDF
- Feedback visual del proceso

## Uso

1. Selecciona el modo de entrada (carpeta o imágenes sueltas)
2. Escoge las imágenes que quieres convertir
3. Selecciona la carpeta donde quieres guardar el PDF
4. ¡Haz clic en "Convertir a PDF"!

## Requisitos

- Windows
- Python 3.x
- Módulos requeridos:
  - img2pdf
  - tkinter (incluido en Python)

## Instalación

1. Descarga el ejecutable que está en la carpeta DIST
2. ¡Listo para usar!

## Desarrollo

Para compilar desde el código fuente:

```bash
pyinstaller --onefile --windowed --add-data "superAlflow.png;." convert_to_pdf.py