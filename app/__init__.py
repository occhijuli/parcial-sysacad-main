import logging
from flask import Flask
import os
try:
    from flask_marshmallow import Marshmallow
except Exception:
    # Permitir ejecución en entornos donde flask_marshmallow no está
    # instalado (por ejemplo, ciertos entornos de CI o tests ligeros).
    class Marshmallow:
        def __init__(self):
            pass

        def init_app(self, app):
            # No-op: las funcionalidades de serialización no están disponibles
            return None

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_hashids import Hashids
from app import blueprints

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
hashids = Hashids()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    # https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)
    migrate.init_app(app, db)
    hashids.init_app(app)
    ma.init_app(app)
    
     # Registrar un converter 'hashid' por defecto si la extensión Hashids
    # no lo hizo (p. ej. en entornos de test con shim). Usamos el
    # IntegerConverter como fallback para aceptar ids numéricos.
    try:
        from werkzeug.routing import IntegerConverter
        if 'hashid' not in app.url_map.converters:
            app.url_map.converters['hashid'] = IntegerConverter
    except Exception:
        # Si por alguna razón no está disponible, seguimos sin registrar;
        # las rutas que usen <hashid:...> fallarán y será visible en tests.
        pass


    blueprints.registrar_blueprints(app)
    
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
