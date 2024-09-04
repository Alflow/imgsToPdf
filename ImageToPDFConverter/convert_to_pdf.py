import img2pdf
import os
import sys
import webbrowser
from tkinter import Tk, Label, Button, filedialog, PhotoImage, Canvas

def convert_images_to_pdf(folder_path, output_pdf):
    images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".png", ".jpg", ".jpeg", ".tiff"))]
    images.sort()
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))

def open_github_profile():
    webbrowser.open("https://github.com/Alflow")

def start_conversion():
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta con imágenes")
    if not folder_path:
        return

    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF como")
    if not output_pdf:
        return

    convert_images_to_pdf(folder_path, output_pdf)
    print(f"PDF creado exitosamente como {output_pdf}")

if __name__ == "__main__":
    root = Tk()
    root.title("ImgsToPDF! By Alflow")
    root.geometry("400x500")
    root.resizable(False, False)

    # Obtener la ruta del directorio donde está el ejecutable o el script
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Cargar la imagen de fondo
    image_path = os.path.join(base_path, "superAlflow.png")
    bg_image = PhotoImage(file=image_path)

    # Crear un Canvas para manejar la imagen de fondo
    canvas = Canvas(root, width=400, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Añadir el título sobre la imagen
    canvas.create_text(200, 50, text="ImgsToPDF! By Alflow", font=("Helvetica", 20, "bold"), fill="white")

    # Botón para iniciar la conversión
    convert_button = Button(root, text="Convertir Imágenes a PDF", command=start_conversion, font=("Helvetica", 14), bg="lightblue", fg="black")
    canvas.create_window(200, 200, window=convert_button)

    github_link = Label(root, text="Visita mi perfil", font=("Helvetica", 12, "underline"), fg="blue", cursor="hand2", bg="black")
    github_link.bind("<Button-1>", lambda e: open_github_profile())
    canvas.create_window(200, 450, window=github_link)

    root.mainloop()
