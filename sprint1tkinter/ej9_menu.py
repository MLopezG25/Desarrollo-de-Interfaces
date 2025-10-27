import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Has pulsado Abrir")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación de ejemplo con menú")

root = tk.Tk()
root.title("Ejercicio 9 - Menu")
root.geometry("300x200")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

root.mainloop()
