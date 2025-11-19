import customtkinter as ctk

class MainView:
    def __init__(self, master):
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Lista de usuarios
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(master)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Detalles del usuario
        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_nombre = ctk.CTkLabel(self.detalles_frame, text="Nombre: ")
        self.label_nombre.pack(pady=5)
        self.label_edad = ctk.CTkLabel(self.detalles_frame, text="Edad: ")
        self.label_edad.pack(pady=5)
        self.label_genero = ctk.CTkLabel(self.detalles_frame, text="Género: ")
        self.label_genero.pack(pady=5)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
