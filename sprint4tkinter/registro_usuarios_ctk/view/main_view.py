import customtkinter as ctk

class MainView:
    def __init__(self, master):
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(master)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Título user
        self.titulo_usuarios = ctk.CTkLabel(self.lista_usuarios_scrollable, text="Usuarios", font=("Arial", 16, "bold"))
        self.titulo_usuarios.pack(pady=(5, 10))
        # botón de añadir usuario
        self.btn_añadir_usuario = ctk.CTkButton(master, text="Añadir Usuario")
        self.btn_añadir_usuario.grid(row=1, column=0, columnspan=2, pady=10)


        # Botón Salir
        self.frame_salir = ctk.CTkFrame(master)
        self.frame_salir.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        self.frame_salir.grid_columnconfigure(0, weight=1)

        self.btn_salir = ctk.CTkButton(
            self.frame_salir, text="Salir",
        )
        self.btn_salir.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        # Detalles del usuario
        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Título detalles
        self.titulo_detalles = ctk.CTkLabel(self.detalles_frame, text="Detalles del Usuario", font=("Arial", 16, "bold"))
        self.titulo_detalles.pack(pady=(5, 10))

        self.label_nombre = ctk.CTkLabel(self.detalles_frame, text="Nombre: ")
        self.label_nombre.pack(pady=5)
        self.label_edad = ctk.CTkLabel(self.detalles_frame, text="Edad: ")
        self.label_edad.pack(pady=5)
        self.label_genero = ctk.CTkLabel(self.detalles_frame, text="Género: ")
        self.label_genero.pack(pady=5)

        # Mostrar avatar
        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="Avatar: ")
        self.avatar_label.pack(pady=5)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            if widget != self.titulo_usuarios:  
                widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)


    def mostrar_detalles_usuario(self, usuario, avatar_image=None):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
        if avatar_image:
            self.avatar_label.configure(image=avatar_image, text="")
        else:
            self.avatar_label.configure(image="", text="Avatar: (sin imagen)")

class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")  # CAMBIO: un poco más alto para el botón cancelar
        self.window.grab_set()  # Modal

        # Nombre
        self.nombre_entry = ctk.CTkEntry(self.window, placeholder_text="Nombre")
        self.nombre_entry.pack(pady=5)

        # Edad
        self.edad_entry = ctk.CTkEntry(self.window, placeholder_text="Edad")
        self.edad_entry.pack(pady=5)

        # CAMBIO: Género con Radiobuttons
        self.genero_var = ctk.StringVar(value="Otro")
        self.genero_label = ctk.CTkLabel(self.window, text="Género:")
        self.genero_label.pack(pady=(10, 0))

        self.genero_m = ctk.CTkRadioButton(self.window, text="Masculino", variable=self.genero_var, value="Masculino")
        self.genero_m.pack(anchor="w", padx=20)
        self.genero_f = ctk.CTkRadioButton(self.window, text="Femenino", variable=self.genero_var, value="Femenino")
        self.genero_f.pack(anchor="w", padx=20)
        self.genero_o = ctk.CTkRadioButton(self.window, text="Otro", variable=self.genero_var, value="Otro")
        self.genero_o.pack(anchor="w", padx=20)

        # CAMBIO: Avatar con OptionMenu
        self.avatar_var = ctk.StringVar(value="avatar1.png")
        self.avatar_label = ctk.CTkLabel(self.window, text="Avatar:")
        self.avatar_label.pack(pady=(10, 0))

        self.avatar1 = ctk.CTkRadioButton(self.window, text="Avatar 1", variable=self.avatar_var, value="avatar1.png")
        self.avatar1.pack(anchor="w", padx=20)
        self.avatar2 = ctk.CTkRadioButton(self.window, text="Avatar 2", variable=self.avatar_var, value="avatar2.png")
        self.avatar2.pack(anchor="w", padx=20)
        self.avatar3 = ctk.CTkRadioButton(self.window, text="Avatar 3", variable=self.avatar_var, value="avatar3.png")
        self.avatar3.pack(anchor="w", padx=20)

        # Botones Guardar y Cancelar
        self.button_frame = ctk.CTkFrame(self.window)
        self.button_frame.pack(pady=15, fill="x")

        self.guardar_button = ctk.CTkButton(self.button_frame, text="Guardar")
        self.guardar_button.pack(side="left", padx=10)

        # CAMBIO: botón Cancelar que cierra la ventana
        self.cancelar_button = ctk.CTkButton(self.button_frame, text="Cancelar", fg_color="gray", hover_color="darkgray",
                                             command=self.window.destroy)
        self.cancelar_button.pack(side="right", padx=10)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),   # CAMBIO: recogemos valor de radiobuttons
            "avatar": self.avatar_var.get()    # CAMBIO: recogemos valor de optionmenu
        }