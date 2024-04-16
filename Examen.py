# Importar la clase base Evento
from Evento import Evento

class Examen(Evento):
    #Constructor declase Examen
    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia

    def __str__(self):
        return f"Tipo: Examen, {super().__str__()}, Materia: {self.materia}"
