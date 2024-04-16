#Importar laclase base
from Evento import Evento

class ReunionEstudio(Evento):
    #Constructor de la clase ReunionEstudio
    def __init__(self, fecha, descripcion, tema):
        super().__init__(fecha, descripcion)
        self.tema = tema

    def __str__(self):
        return f"Tipo: Reunión de Estudio, {super().__str__()}, Tema: {self.tema}"
