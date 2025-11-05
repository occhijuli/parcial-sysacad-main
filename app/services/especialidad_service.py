from app.models import Especialidad
from app.repositories import EspecialidadRepository

class EspecialidadService:

    @staticmethod
    def crear(especialidad):
        EspecialidadRepository.crear(especialidad)

    @staticmethod
    def buscar_por_id(id: int) -> Especialidad:
        return EspecialidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Especialidad]:
        return EspecialidadRepository.buscar_todos()

    @staticmethod
    def actualizar(id: int, especialidad: Especialidad) -> Especialidad:
        especialidad_existente = EspecialidadRepository.buscar_por_id(id)
        if not especialidad_existente:
            return None
        especialidad_existente.nombre = especialidad.nombre
        especialidad_existente.letra = especialidad.letra
        especialidad_existente.observacion = especialidad.observacion
        especialidad_existente.tipoespecialidad = especialidad.tipoespecialidad
        especialidad_existente.facultad = especialidad.facultad
        return EspecialidadRepository.actualizar(especialidad_existente)
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return EspecialidadRepository.borrar_por_id(id)

    @staticmethod
    def obtener_alumnos_y_facultad(id: int) -> dict:
        """Devuelve un diccionario con la facultad y la lista de alumnos
        de la especialidad indicada.
        """
        especialidad = EspecialidadRepository.buscar_por_id(id)
        if not especialidad:
            return None
        # import para evitar dependencias cíclicas
        from app.services.alumno_service import AlumnoService

        alumnos = AlumnoService.buscar_por_especialidad(id)
        facultad = especialidad.facultad
        return {
            'facultad': facultad,
            'alumnos': alumnos
        }
