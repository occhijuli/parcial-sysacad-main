import unittest
import os
from app import create_app
from app import db
from test.instancias import nuevaespecialidad, nuevoalumno
from app.services.especialidad_service import EspecialidadService


class EspecialidadServiceTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_obtener_alumnos_y_facultad(self):
        esp = nuevaespecialidad()
        a1 = nuevoalumno(nombre='Ana', apellido='Lopez', nrodocumento='111', especialidad=esp)
        a2 = nuevoalumno(nombre='Luis', apellido='Gomez', nrodocumento='222', especialidad=esp)

        result = EspecialidadService.obtener_alumnos_y_facultad(esp.id)
        self.assertIsNotNone(result)
        self.assertIn('facultad', result)
        self.assertIn('alumnos', result)
        self.assertEqual(len(result['alumnos']), 2)
        ids = [a.id for a in result['alumnos']]
        self.assertIn(a1.id, ids)
        self.assertIn(a2.id, ids)


if __name__ == '__main__':
    unittest.main()
