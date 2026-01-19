from django.test import TestCase
from webapp.models import Sala

class SalaModelTest(TestCase):
    def test_create_sala(self):
        """
        Test creating a Sala with the specified JSON structure.
        """
        horarios = {
            "segunda": [{"from": 9, "to": 17}],
            "terca": [{"from": 10, "to": 18}]
        }
        sala = Sala.objects.create(nome="Sala de Reunião 1", horarios_disponiveis=horarios)

        self.assertEqual(sala.nome, "Sala de Reunião 1")
        self.assertEqual(sala.horarios_disponiveis, horarios)
        self.assertTrue("segunda" in sala.horarios_disponiveis)
        self.assertEqual(sala.horarios_disponiveis["segunda"][0]["from"], 9)
