"""Shim para `flask_hashids` cuando la dependencia no está instalada.

Esto permite ejecutar la suite de tests en entornos mínimos sin instalar
la dependencia externa. Proporciona implementaciones mínimas de
`Hashids` y `HashidMixin` usadas por el proyecto.
Issue relacionada: #6
"""

class Hashids:
    def __init__(self, min_length: int = 8, salt: str = ''):
        self.min_length = min_length
        self.salt = salt

    def init_app(self, app):
        # no-op para tests que no necesitan hashids funcional
        return None

    def encode(self, *vals):
        # devolver representación simple para evitar errores
        try:
            return "-".join(str(v) for v in vals)
        except Exception:
            return None

    def decode(self, val):
        # intentar extraer enteros si fue generado por encode shim
        if not val:
            return ()
        parts = val.split('-')
        out = []
        for p in parts:
            try:
                out.append(int(p))
            except Exception:
                pass
        return tuple(out)


class HashidMixin:
    """Mixin mínimo que expone una propiedad `hashid` usada por tests.

    No implementa seguridad, sólo evita errores cuando la librería
    real no está disponible.
    """
    @property
    def hashid(self):
        ident = getattr(self, 'id', None)
        if ident is None:
            return None
        return str(ident)
