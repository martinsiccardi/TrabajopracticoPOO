#Importar las clases
from Evento import Evento
from Examen import Examen
from Trabajo_Practico import TrabajoPractico
from Reunion_Estudio import ReunionEstudio

class Agenda:
    def __init__(self):#Constructor
        self.eventos = []

    def agregar_evento(self, evento):# Método para agregar un evento a la agenda
        self.eventos.append(evento)

    def mostrar_eventos(self):# Método para mostrar todos los eventos en la agenda
        for evento in self.eventos:
            print(evento)

    def eliminar_evento_por_descripcion(self, descripcion):# Método para eliminar un evento de la agenda
        eventos_restantes = [evento for evento in self.eventos if evento.descripcion != descripcion]
        if len(eventos_restantes) < len(self.eventos):
            print(f"Evento con descripción '{descripcion}' eliminado.")
        else:
            print(f"No se encontró ningún evento con descripción '{descripcion}'.")
        self.eventos = eventos_restantes

# Función para ingresar eventos
def ingresar_evento():
    tipo_evento = input("Ingrese el tipo de evento (Examen, TrabajoPractico, ReunionEstudio): ").strip().lower()

    fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ")
    descripcion = input("Ingrese una descripción del evento: ")

    if tipo_evento == "examen":
        materia = input("Ingrese la materia del examen: ")
        return Examen(fecha, descripcion, materia)
    elif tipo_evento == "trabajopractico":
        asignatura = input("Ingrese la asignatura del trabajo práctico: ")
        return TrabajoPractico(fecha, descripcion, asignatura)
    elif tipo_evento == "reunionestudio":
        tema = input("Ingrese el tema de la reunión de estudio: ")
        return ReunionEstudio(fecha, descripcion, tema)
    else:
        print("Tipo de evento no válido.")
        return None


# Uso alfinalizar
if __name__ == "__main__":
    agenda = Agenda()

    while True:
        evento = ingresar_evento()
        if evento:
            agenda.agregar_evento(evento)
            continuar = input("¿Desea agregar otro evento? (s/n): ").strip().lower()
            if continuar != "s":
                break

    print("\nAgenda:")
    agenda.mostrar_eventos()

    opcion_borrar = input("\n¿Desea borrar algún evento de la agenda? (s/n): ").strip().lower()
    if opcion_borrar == "s":
        descripcion_eliminar = input("Ingrese la descripción del evento que desea eliminar: ")
        agenda.eliminar_evento_por_descripcion(descripcion_eliminar)
        print("\nAgenda actualizada:")
        agenda.mostrar_eventos()
    else:
        print("La agenda no ha sido modificada.")
