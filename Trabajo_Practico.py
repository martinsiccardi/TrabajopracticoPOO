from Evento import Evento

class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, asignatura):
        super().__init__(fecha, descripcion)
        self.asignatura = asignatura

    def __str__(self):
        return f"Tipo: Trabajo Práctico, {super().__str__()}, Asignatura: {self.asignatura}"
