import unittest
from arbol import Arbol


class TestArbol(unittest.TestCase):
    def setUp(self):
        self.a1: Arbol = Arbol(
            float(-58.4367808405),
            float(-34.6664550879),
            "18003891",
            "Fraxinus pennsylvanica",
            "VILLA SOLDATI",
            "Beron De Astrada",
            "0",
        )
        self.a2: Arbol = Arbol(
            float(-58.394875194099995),
            float(-34.6381752804),
            "33012984",
            "Acer negundo",
            "PARQUE PATRICIOS",
            "Monasterio",
            "0",
        )
        self.a3: Arbol = Arbol(
            float(-58.4316972139),
            float(-34.5718077953),
            "39003513",
            "Tecoma stans",
            "PALERMO",
            "Baez",
            "348",
        )
        self.a4: Arbol = Arbol(
            3.0, 
            4.0, 
            "101", 
            "Sauce", 
            "JUANA KOSLAY", 
            "Junin", 
            "605"
        )
        self.a5: Arbol = Arbol(
            6.0,
            8.0,
            "102",
            "Sauce",
            "JUANA KOSLAY",
            "Junin",
            "750"
        )
        self.a6: Arbol = Arbol(
            120.0,
            199.0,
            "103",
            "Sauce",
            "JUANA KOSLAY",
            "Junin",
            "823"
        )

    def test_id(self):
        self.assertEqual(str(self.a1), "18003891")
        self.assertEqual(str(self.a2), "33012984")
        self.assertEqual(str(self.a3), "39003513")
        self.assertEqual(str(self.a4), "101")
        self.assertEqual(str(self.a5), "102")
        self.assertEqual(str(self.a6), "103")

    def test_distancia(self):
        self.assertAlmostEqual(self.a4.distancia(0.0, 0.0), 5.0)
        self.assertAlmostEqual(self.a5.distancia(0.0, 0.0), 10.0)
        self.assertAlmostEqual(self.a6.distancia(100.0, 100.0), 101.0)

    def test_atributos(self):
        self.assertEqual(self.a1.long, float(-58.4367808405))
        self.assertEqual(self.a1.lat, float(-34.6664550879))
        self.assertEqual(self.a1.especie, "Fraxinus pennsylvanica")
        self.assertEqual(self.a1.barrio, "VILLA SOLDATI")
        self.assertEqual(self.a1.direccion, "Beron De Astrada 0")

        self.assertEqual(self.a4.long, 3.0)
        self.assertEqual(self.a4.lat, 4.0)
        self.assertEqual(self.a4.especie, "Sauce")
        self.assertEqual(self.a4.barrio, "JUANA KOSLAY")
        self.assertEqual(self.a4.direccion, "Junin 605")

    def test_igualdad(self):
        copia_a2: Arbol = Arbol(
            float(-58.394875194099995),
            float(-34.6381752804),
            "33012984",
            "Acer negundo",
            "PARQUE PATRICIOS",
            "Monasterio",
            "0",
        )
        self.assertEqual(self.a2, copia_a2)
        copia_a3: Arbol = Arbol(
            float(-58.4316972139),
            float(-34.5718077953),
            "39003513",
            "Tecoma stans",
            "PALERMO",
            "Baez",
            "348",
        )
        self.assertEqual(self.a3, copia_a3)


unittest.main()
