import csv

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str = ""):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()
        self.cargar_csv()   #

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 30, "Femenino", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 45, "Masculino", "avatar2.png"))
        self._usuarios.append(Usuario("Sofía Romero", 22, "Femenino", "avatar3.png"))

    def listar(self):
        return list(self._usuarios)

    def guardar_csv(self, ruta="usuarios.csv"):
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["nombre", "edad", "genero", "avatar"])
            for u in self._usuarios:
                escritor.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta="usuarios.csv"):
        try:
            with open(ruta, "r", newline="", encoding="utf-8") as f:
                lector = csv.reader(f)
                next(lector)  # Salto de cabecera
                self._usuarios.clear()
                for fila in lector:
                    try:
                        nombre, edad, genero, avatar = fila
                        self._usuarios.append(Usuario(nombre, int(edad), genero, avatar))
                    except Exception as e:
                        print(f"Error en línea CSV: {e}")
        except FileNotFoundError:

            self._usuarios.clear()
