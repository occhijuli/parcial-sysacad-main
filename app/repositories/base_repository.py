from app import db


class BaseRepository:
    """Repositorio base con métodos CRUD reutilizables.

    Objetivo: reducir código duplicado entre repositorios simples que sólo
    realizan operaciones básicas sobre `db.session`.
    """

    @staticmethod
    def crear(entity):
        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def buscar_por_id(model, id: int):
        return db.session.query(model).filter_by(id=id).first()

    @staticmethod
    def buscar_todos(model):
        return db.session.query(model).all()

    @staticmethod
    def actualizar(entity):
        db.session.merge(entity)
        db.session.commit()
        return entity

    @staticmethod
    def borrar_por_id(model, id: int) -> bool:
        obj = db.session.query(model).filter_by(id=id).first()
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
