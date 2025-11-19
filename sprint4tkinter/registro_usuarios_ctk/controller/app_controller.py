from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView

class AppController:
    def __init__(self, root):
        self.root = root
        self.modelo = GestorUsuarios()
        self.vista = MainView(root)

        # Botón de salir
        self.vista.btn_salir.configure(command=self.salir)

        # conectar botón de añadir usuario
        self.vista.btn_añadir_usuario.configure(command=self.abrir_ventana_añadir)

        # Avatares
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.avatar_images = {}

        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.vista.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuarios = self.modelo.listar()
        if 0 <= indice < len(usuarios):
            usuario = usuarios[indice]
            avatar_image = None
            # Cargar la imagen de avatar si tiene
            if usuario.avatar:
                try:
                    img_path = self.ASSETS_PATH / usuario.avatar
                    avatar_image = ctk.CTkImage(Image.open(img_path), size=(100, 100))
                    self.avatar_images[usuario.nombre] = avatar_image
                    self.vista.avatar_label.configure(image=avatar_image, text="")
                except Exception:
                    avatar_image = None
            self.vista.mostrar_detalles_usuario(usuario, avatar_image)

    # Abrir ventana de añadir usuario
    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.root)
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()
        try:
            edad = int(data["edad"])
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")
            return

        nuevo_usuario = Usuario(data["nombre"], edad, data["genero"], data["avatar"])
        self.modelo._usuarios.append(nuevo_usuario)
        self.refrescar_lista_usuarios()
        add_view.window.destroy()

    def salir(self):
        self.root.destroy()
