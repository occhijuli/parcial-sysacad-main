from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(HashidMixin, db.Model):
    __tablename__ = 'tipodocumentos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni: int = db.Column(db.Integer, nullable=True)
    libreta_civica: str = db.Column(db.String(50), nullable=True)
    libreta_enrolamiento: str = db.Column(db.String(50), nullable=True)
    pasaporte: str = db.Column(db.String(50), nullable=True)