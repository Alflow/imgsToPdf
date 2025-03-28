import img2pdf
import os
import sys
import webbrowser
from tkinter import Tk, Label, Button, filedialog, PhotoImage, Canvas, StringVar, Radiobutton

def convert_images_to_pdf(images_list, output_pdf):
    images_list.sort()
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images_list))

def start_conversion_folder():
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta con imágenes")
    if not folder_path:
        return

    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF como")
    if not output_pdf:
        return

    images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".png", ".jpg", ".jpeg", ".tiff"))]
    convert_images_to_pdf(images, output_pdf)
    print(f"PDF creado exitosamente como {output_pdf}")

def start_conversion_files():
    images = filedialog.askopenfilenames(
        title="Selecciona las imágenes",
        filetypes=[
            ("Imágenes", "*.png *.jpg *.jpeg *.tiff"),
            ("Todos los archivos", "*.*")
        ]
    )
    if not images:
        return

    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF como")
    if not output_pdf:
        return

    convert_images_to_pdf(images, output_pdf)
    print(f"PDF creado exitosamente como {output_pdf}")

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

    # Variables globales para almacenar las selecciones
    selected_images = []
    output_path = ""

    def select_source():
        option = source_var.get()
        if option == "folder":
            select_folder()
        else:
            select_files()

    def select_folder():
        global selected_images
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta con imágenes")
        if folder_path:
            selected_images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".png", ".jpg", ".jpeg", ".tiff"))]
            if selected_images:
                status_label.config(text=f"{len(selected_images)} imágenes seleccionadas")
            else:
                status_label.config(text="No se encontraron imágenes")

    def select_files():
        global selected_images
        images = filedialog.askopenfilenames(
            title="Selecciona las imágenes",
            filetypes=[
                ("Imágenes", "*.png *.jpg *.jpeg *.tiff"),
                ("Todos los archivos", "*.*")
            ]
        )
        if images:
            selected_images = list(images)  # Convertir a lista para asegurar compatibilidad
            status_label.config(text=f"{len(selected_images)} imágenes seleccionadas")

    def select_output():
        global output_path
        output_path = filedialog.askdirectory(title="Selecciona donde guardar el PDF")
        if output_path:
            output_label.config(text=f"PDF se guardará en: {output_path}")

    def convert():
        if not selected_images:
            status_label.config(text="¡Selecciona imágenes primero!")
            return
        if not output_path:
            status_label.config(text="¡Selecciona destino del PDF!")
            return
        
        pdf_name = os.path.join(output_path, "converted.pdf")
        try:
            convert_images_to_pdf(selected_images, pdf_name)
            status_label.config(text=f"¡PDF creado exitosamente!")
        except Exception as e:
            status_label.config(text=f"Error al crear PDF: {str(e)}")

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

    # Estilo para el frame del selector
    select_frame = Label(root, bg='#2c3e50', width=30, height=4)
    canvas.create_window(200, 180, window=select_frame)

    # Variable para el selector
    source_var = StringVar(value="folder")

    # Opciones del selector con estilo moderno
    folder_radio = Radiobutton(select_frame, text="Carpeta completa", variable=source_var, 
                             value="folder", bg='#2c3e50', fg='white',
                             selectcolor='#34495e', activebackground='#2c3e50',
                             activeforeground='#3498db', font=('Helvetica', 12))
    folder_radio.pack(pady=5)

    files_radio = Radiobutton(select_frame, text="Imágenes sueltas", variable=source_var,
                            value="files", bg='#2c3e50', fg='white',
                            selectcolor='#34495e', activebackground='#2c3e50',
                            activeforeground='#3498db', font=('Helvetica', 12))
    files_radio.pack(pady=5)

    # Botón de selección unificado
    select_button = Button(root, text="Seleccionar Imágenes", command=select_source,
                         bg="#3498db", fg="white", activebackground="#2980b9",
                         font=('Helvetica', 14, 'bold'), width=20,
                         relief='raised', borderwidth=3)
    canvas.create_window(200, 250, window=select_button)

    # Botón para seleccionar destino
    output_button = Button(root, text="Quiero el PDF en la carpeta...", command=select_output,
                         bg="#2ecc71", fg="white", activebackground="#27ae60",
                         font=('Helvetica', 14), width=20,
                         relief='raised', borderwidth=3)
    canvas.create_window(200, 310, window=output_button)

    # Etiquetas de estado
    status_label = Label(root, text="", font=("Helvetica", 12), bg="black", fg="white")
    canvas.create_window(200, 340, window=status_label)

    output_label = Label(root, text="", font=("Helvetica", 12), bg="black", fg="white")
    canvas.create_window(200, 370, window=output_label)

    # Botón de conversión
    convert_button = Button(root, text="¡Convertir a PDF!", command=convert,
                          bg="#e67e22", fg="white", activebackground="#d35400",
                          font=('Helvetica', 16, 'bold'), width=15,
                          relief='raised', borderwidth=4)
    canvas.create_window(200, 410, window=convert_button)

    # Link a GitHub
    github_link = Label(root, text="Visita mi perfil", font=("Helvetica", 12, "underline"),
                       fg="#3498db", cursor="hand2", bg="black")
    github_link.bind("<Button-1>", lambda e: open_github_profile())
    canvas.create_window(200, 450, window=github_link)

    root.mainloop()
