import tkinter as tk
from tkinter import messagebox
import random

class Juego:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        self.jugador_puntos = 0
        self.maquina_puntos = 0
        self.rondas_validas = 0
        self.opciones = ["piedra", "papel", "tijera"]

        self.jugador_var = tk.StringVar()
        self.maquina_var = tk.StringVar()
        self.resultado_var = tk.StringVar()
        self.marcador_var = tk.StringVar()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_jugador = tk.Label(self.frame, textvariable=self.jugador_var, width=30)
        self.label_jugador.grid(row=0, column=0)

        self.label_maquina = tk.Label(self.frame, textvariable=self.maquina_var, width=30)
        self.label_maquina.grid(row=0, column=1)

        self.label_resultado = tk.Label(self.frame, textvariable=self.resultado_var, width=60)
        self.label_resultado.grid(row=1, column=0, columnspan=2)

        self.label_marcador = tk.Label(self.frame, textvariable=self.marcador_var, width=60)
        self.label_marcador.grid(row=2, column=0, columnspan=2)

        self.botones_frame = tk.Frame(root)
        self.botones_frame.pack(pady=10)

        for i, opcion in enumerate(self.opciones):
            tk.Button(self.botones_frame, text=opcion.capitalize(), width=10,
                      command=lambda o=opcion: self.jugar(o)).grid(row=0, column=i)

        self.boton_nuevo = tk.Button(root, text="Nuevo juego", command=self.reiniciar)
        self.boton_nuevo.pack(pady=5)

        self.boton_salir = tk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack(pady=5)

        self.actualizar_marcador()

    def jugar(self, eleccion_jugador):
        if self.jugador_puntos == 3 or self.maquina_puntos == 3:
            return

        eleccion_maquina = random.choice(self.opciones)
        self.jugador_var.set(f"Jugador: {eleccion_jugador}")
        self.maquina_var.set(f"Máquina: {eleccion_maquina}")

        resultado = self.evaluar(eleccion_jugador, eleccion_maquina)
        self.resultado_var.set(resultado)
        self.actualizar_marcador()

        if self.jugador_puntos == 3 or self.maquina_puntos == 3:
            final = "Ganaste" if self.jugador_puntos == 3 else "Perdiste"
            messagebox.showinfo("Fin de partida", final)

    def evaluar(self, j, m):
        if j == m:
            return "Empate"
        gana = (j == "piedra" and m == "tijera") or \
               (j == "papel" and m == "piedra") or \
               (j == "tijera" and m == "papel")
        if gana:
            self.jugador_puntos += 1
            self.rondas_validas += 1
            return f"{j.capitalize()} gana a {m}. Punto para ti."
        else:
            self.maquina_puntos += 1
            self.rondas_validas += 1
            return f"{m.capitalize()} gana a {j}. Punto para él."

    def actualizar_marcador(self):
        self.marcador_var.set(f"Jugador: {self.jugador_puntos}  |  Máquina: {self.maquina_puntos}")

    def reiniciar(self):
        self.jugador_puntos = 0
        self.maquina_puntos = 0
        self.rondas_validas = 0
        self.jugador_var.set("")
        self.maquina_var.set("")
        self.resultado_var.set("")
        self.actualizar_marcador()

if __name__ == "__main__":
    root = tk.Tk()
    app = Juego(root)
    root.mainloop()
