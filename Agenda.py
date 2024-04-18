from Evento import Evento
from Examen import Examen
from Trabajo_Practico import TrabajoPractico
from Reunion_Estudio import ReunionEstudio

class Agenda:
    def __init__(self):
        # Constructor 
        self.eventos = []  # Inicializar lista de eventos

    def agregar_evento(self, evento):
        # Método para agregar un evento a la agenda
        self.eventos.append(evento)

    def mostrar_eventos(self):
        # Método para mostrar todos los eventos en la agenda
        if self.eventos:
            print("Eventos en la agenda:")
            for i, evento in enumerate(self.eventos, 1):
                print(f"{i}. {evento}")  
        else:
            print("No hay eventos en la agenda.")

    def eliminar_evento_por_descripcion(self, descripcion):
        # Método para eliminar un evento de la agenda 
        eventos_restantes = [evento for evento in self.eventos if evento.descripcion != descripcion]  # Filtrar eventos que no coinciden con la descripción
        if len(eventos_restantes) < len(self.eventos):
            # Verificar si se eliminó algún evento
            print(f"Evento con descripción '{descripcion}' eliminado.")
        else:
            print(f"No se encontró ningún evento con descripción '{descripcion}'.")
        self.eventos = eventos_restantes  # Actualizar la lista de eventos

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


# Menú principal del programa
def menu_principal():
    print("\nBienvenido a la Agenda\n")
    print("1. Ver eventos existentes")
    print("2. Ingresar un nuevo evento")
    print("3. Eliminar un evento")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")
    return opcion

# Ejemplo de uso
if __name__ == "__main__":
    agenda = Agenda()  # Crear una instancia de la clase Agenda

    while True:
        opcion = menu_principal()

        if opcion == "1":
            agenda.mostrar_eventos()  # Mostrar todos los eventos en la agenda
        elif opcion == "2":
            evento = ingresar_evento()  # Solicitar al usuario que ingrese un evento
            if evento:
                agenda.agregar_evento(evento)  # Agregar el evento a la agenda
                print("\nEvento agregado a la agenda.")
        elif opcion == "3":
            if agenda.eventos:
                descripcion_eliminar = input("\nIngrese la descripción del evento que desea eliminar: ")
                agenda.eliminar_evento_por_descripcion(descripcion_eliminar)  # Eliminar evento por descripción
            else:
                print("\nNo hay eventos en la agenda.")
        elif opcion == "4":
            print("Gracias por usar la Agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
