from app.models import TipoDocumento
from app.repositories.base_repository import BaseRepository


class TipoDocumentoRepository:
    """Repositorio específico para TipoDocumento que delega operaciones
    al `BaseRepository` para evitar duplicación.
    Issue relacionada: #4
    """

    @staticmethod
    def crear(tipodocumento):
        return BaseRepository.crear(tipodocumento)

    @staticmethod
    def buscar_por_id(id: int):
        return BaseRepository.buscar_por_id(TipoDocumento, id)

    @staticmethod
    def buscar_todos():
        return BaseRepository.buscar_todos(TipoDocumento)

    @staticmethod
    def actualizar(tipodocumento) -> TipoDocumento:
        return BaseRepository.actualizar(tipodocumento)

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return BaseRepository.borrar_por_id(TipoDocumento, id)

