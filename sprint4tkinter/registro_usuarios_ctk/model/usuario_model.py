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

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 30, "Femenino", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 45, "Masculino", "avatar2.png"))
        self._usuarios.append(Usuario("Sofía Romero", 22, "Femenino", "avatar3.png"))

    def listar(self):
        return list(self._usuarios)
