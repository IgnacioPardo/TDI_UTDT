import unittest

# Importamos el codigo a testear.
from dataset import DataSetArboreo
from arbol import Arbol
from typing import Set, List, Dict

####################################################################


class TestDataSetArboreo(unittest.TestCase):
    def setUp(self):
        # Inicialización del testing.
        self.dt1: DataSetArboreo = DataSetArboreo("arbolado_test1.csv")
        self.dt2: DataSetArboreo = DataSetArboreo("arbolado_test2.csv")
        self.dt3: DataSetArboreo = DataSetArboreo("arbolado_test3.csv")

    def test_dt1_creo_dataset_no_vacio(self):
        size: int = self.dt1.tamano()
        self.assertTrue(size > 0)
        self.assertEqual(size, 24)

    def test_dt1_especies_en_dt(self):
        gt: Set[str] = {
            "Ficus benjamina",
            "Fraxinus pennsylvanica",
            "Salix babylonica",
            "Fraxinus excelsior",
            "Tilia viridis subsp. x moltkei",
            "Platanus x acerifolia",
            "Prunus cerasifera",
            "Acer negundo",
            "Ligustrum lucidum",
        }
        es: Set[str] = self.dt1.especies()

        self.assertEqual(es, gt)

    def test_dt1_barrios_en_dt(self):
        gt: Set[str] = {
            "VILLA URQUIZA",
            "SAN NICOLAS",
            "PARQUE PATRICIOS",
            "RECOLETA",
            "VILLA DEL PARQUE",
            "CONSTITUCION",
        }
        br: Set[str] = self.dt1.barrios()

        self.assertEqual(br, gt)

    def test_dt1_arboles_de_la_especie_Fraxinus_pennsylvanica(self):
        gt: List[Arbol] = [
            Arbol(
                float(-58.3890587967),
                float(-34.6200256156),
                "2430",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "1609",
            ),
            Arbol(
                float(-58.389211331700004),
                float(-34.6200342718),
                "2431",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "1617",
            ),
            Arbol(
                float(-58.389607770299996),
                float(-34.6200566868),
                "2434",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "1655",
            ),
            Arbol(
                float(-58.3897390443),
                float(-34.6200641577),
                "2436",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "0",
            ),
            Arbol(
                float(-58.3898303037),
                float(-34.6200693508),
                "2437",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "1673",
            ),
            Arbol(
                float(-58.389912840600005),
                float(-34.6200739977),
                "2438",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Calvo,Carlos",
                "0",
            ),
            Arbol(
                float(-58.3901634566),
                float(-34.6200181701),
                "2440",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Solis",
                "994",
            ),
            Arbol(
                float(-58.3901737657),
                float(-34.6198259035),
                "2442",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Solis",
                "0",
            ),
            Arbol(
                float(-58.3901766495),
                float(-34.6197701975),
                "2443",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Solis",
                "974",
            ),
            Arbol(
                float(-58.3901804185),
                float(-34.619699799),
                "2444",
                "Fraxinus pennsylvanica",
                "CONSTITUCION",
                "Solis",
                "966",
            ),
            Arbol(
                float(-58.39485770140001),
                float(-34.638227552800004),
                "33012983",
                "Fraxinus pennsylvanica",
                "PARQUE PATRICIOS",
                "Monasterio",
                "0",
            ),
        ]
        ae: List[Arbol] = self.dt1.arboles_de_la_especie("Fraxinus pennsylvanica")

        self.assertEqual(len(ae), 11)
        self.assertTrue(list_equals(ae, gt))

    def test_dt1_arboles_de_la_especie_Acer_negundo(self):
        gt: List[Arbol] = [
            Arbol(
                float(-58.3895252334),
                float(-34.6200520397),
                "2433",
                "Acer negundo",
                "CONSTITUCION",
                "Calvo,Carlos",
                "0",
            ),
            Arbol(
                float(-58.3948239188),
                float(-34.638328312199995),
                "33012982",
                "Acer negundo",
                "PARQUE PATRICIOS",
                "Monasterio",
                "0",
            ),
            Arbol(
                float(-58.394875194099995),
                float(-34.6381752804),
                "33012984",
                "Acer negundo",
                "PARQUE PATRICIOS",
                "Monasterio",
                "0",
            ),
        ]
        ae: List[Arbol] = self.dt1.arboles_de_la_especie("Acer negundo")

        self.assertEqual(len(ae), 3)
        self.assertTrue(list_equals(ae, gt))

    def test_dt1_cantidad_por_especie_m1(self):
        m: int = 1
        cpe: Dict[str, int] = self.dt1.cantidad_por_especie(m)
        self.assertEqual(len(cpe), 5)
        k: str
        v: int
        for v in cpe.values():
            self.assertTrue(v > m)
        self.assertEqual(cpe["Fraxinus pennsylvanica"], 11)
        self.assertEqual(cpe["Acer negundo"], 3)

    def test_dt1_cantidad_por_especie_m2(self):
        m: int = 2
        cpe: Dict[str, int] = self.dt1.cantidad_por_especie(m)
        self.assertEqual(len(cpe), 2)
        k: str
        v: int
        for v in cpe.values():
            self.assertTrue(v > m)
        self.assertEqual(cpe["Fraxinus pennsylvanica"], 11)

    def test_dt1_cantidad_por_especie_m5(self):
        m: int = 5
        cpe: Dict[str, int] = self.dt1.cantidad_por_especie(m)
        self.assertEqual(len(cpe), 1)
        k: str
        v: int
        for v in cpe.values():
            self.assertTrue(v > m)
        self.assertEqual(cpe["Fraxinus pennsylvanica"], 11)

    def test_dt1_arbol_mas_cercano(self):
        gt: Arbol = Arbol(
            float(-58.3901804185),
            float(-34.619699799),
            "2444",
            "Fraxinus pennsylvanica",
            "CONSTITUCION",
            "Solis",
            "966",
        )

        lat: float = 58.38960
        long: float = -34.62005
        closest: Arbol = self.dt1.arbol_mas_cercano("Fraxinus pennsylvanica", lat, long)

        self.assertEqual(closest, gt)

    def test_dt2_creo_dataset_vacio(self):
        size: int = self.dt2.tamano()
        self.assertEqual(size, 0)

    def test_dt2_especies_en_dt(self):
        gt: Set[str] = set()
        es: Set[str] = self.dt2.especies()

        self.assertEqual(es, gt)

    def test_dt2_barrios_en_dt(self):
        gt: Set[str] = set()
        br: Set[str] = self.dt2.barrios()

        self.assertEqual(br, gt)

    def test_dt3_creo_dataset_no_vacio(self):
        size: int = self.dt3.tamano()
        self.assertTrue(size > 0)
        self.assertEqual(size, 24)

    def test_dt3_especies_en_dt(self):
        gt: Set[str] = {
            "Melia azeradach",
            "Fraxinus excelsior",
            "Ligustrum lucidum for. aureo-variegatum",
            "Robinia pseudoacacia",
            "Poecilanthe parviflora",
            "Jacarandá mimosifolia",
            "Betula alba",
            "Tecoma stans",
            "Fraxinus pennsylvanica",
            "Platanus x acerifolia",
            "Acacia dealbata",
            "Albizia julibrissin",
            "Styphnolobium japonicum",
        }
        es: Set[str] = self.dt3.especies()

        self.assertEqual(es, gt)

    def test_dt3_barrios_en_dt(self):
        gt: Set[str] = {
            "BOEDO",
            "FLORES",
            "SAAVEDRA",
            "RETIRO",
            "VILLA LUGANO",
            "VILLA SOLDATI",
            "LINIERS",
            "ALMAGRO",
            "CABALLITO",
            "NUEVA POMPEYA",
            "VILLA DEL PARQUE",
            "PARQUE AVELLANEDA",
            "VILLA URQUIZA",
            "RECOLETA",
            "PALERMO",
            "BARRACAS",
            "BELGRANO",
        }
        br: Set[str] = self.dt3.barrios()

        self.assertEqual(br, gt)

    def test_dt3_arboles_de_la_especie_Fraxinus_pennsylvanica(self):
        gt: List[Arbol] = [
            Arbol(
                float(-58.3984481436),
                float(-34.5855826819),
                "17844",
                "Fraxinus pennsylvanica",
                "RECOLETA",
                "Galileo",
                "0",
            ),
            Arbol(
                float(-58.4304670374),
                float(-34.609690166),
                "127031",
                "Fraxinus pennsylvanica",
                "CABALLITO",
                "Rio De Janeiro",
                "542",
            ),
            Arbol(
                float(-58.4201815508),
                float(-34.6166394399),
                "24456",
                "Fraxinus pennsylvanica",
                "ALMAGRO",
                "Quito",
                "0",
            ),
            Arbol(
                float(-58.4180792828),
                float(-34.631535435500005),
                "79126",
                "Fraxinus pennsylvanica",
                "BOEDO",
                "Garay  Juan De Av.",
                "3813",
            ),
            Arbol(
                float(-58.4367808405),
                float(-34.6664550879),
                "18003891",
                "Fraxinus pennsylvanica",
                "VILLA SOLDATI",
                "Beron De Astrada",
                "0",
            ),
            Arbol(
                float(-58.4377293317),
                float(-34.6671808374),
                "18003896",
                "Fraxinus pennsylvanica",
                "VILLA SOLDATI",
                "Beron De Astrada",
                "0",
            ),
            Arbol(
                float(-58.4155265172),
                float(-34.6468832422),
                "72695",
                "Fraxinus pennsylvanica",
                "NUEVA POMPEYA",
                "Ochoa  Enrique",
                "0",
            ),
            Arbol(
                float(-58.5265410805),
                float(-34.6488576023),
                "47000109",
                "Fraxinus pennsylvanica",
                "LINIERS",
                "Paula Y Rodriguez Alves  Jose De",
                "0",
            ),
        ]
        ae: List[Arbol] = self.dt3.arboles_de_la_especie("Fraxinus pennsylvanica")

        self.assertEqual(len(ae), 8)
        self.assertTrue(list_equals(ae, gt))

    def test_dt3_arboles_de_la_especie_Acer_negundo(self):
        gt: List[Arbol] = [
            Arbol(
                float(-58.492648672399994),
                float(-34.5603693336),
                "28001531",
                "Tecoma stans",
                "SAAVEDRA",
                "Galvan",
                "0",
            ),
            Arbol(
                float(-58.4316972139),
                float(-34.5718077953),
                "39003513",
                "Tecoma stans",
                "PALERMO",
                "Baez",
                "348",
            ),
        ]
        ae: List[Arbol] = self.dt3.arboles_de_la_especie("Tecoma stans")

        self.assertEqual(len(ae), 2)
        self.assertTrue(list_equals(ae, gt))

    def test_dt3_cantidad_por_especie_m1(self):
        m: int = 1
        cpe: Dict[str, int] = self.dt3.cantidad_por_especie(m)
        self.assertEqual(len(cpe), 5)
        k: str
        v: int
        for v in cpe.values():
            self.assertTrue(v > m)
        self.assertEqual(cpe["Tecoma stans"], 2)
        self.assertEqual(cpe["Melia azeradach"], 2)
        self.assertEqual(cpe["Fraxinus pennsylvanica"], 8)
        self.assertEqual(cpe["Fraxinus excelsior"], 2)
        self.assertEqual(cpe["Jacarandá mimosifolia"], 2)

    def test_dt3_cantidad_por_especie_m2(self):
        m: int = 2
        cpe: Dict[str, int] = self.dt3.cantidad_por_especie(m)
        self.assertEqual(len(cpe), 1)
        k: str
        v: int
        for v in cpe.values():
            self.assertTrue(v > m)
        self.assertEqual(cpe["Fraxinus pennsylvanica"], 8)

    def test_dt3_arbol_mas_cercano(self):
        gt: Arbol = Arbol(
            float(-58.4316972139),
            float(-34.5718077953),
            "39003513",
            "Tecoma stans",
            "PALERMO",
            "Baez",
            "348",
        )

        lat: float = -58.49264867239999
        long: float = -34.560369333
        closest: Arbol = self.dt3.arbol_mas_cercano("Tecoma stans", lat, long)

        self.assertEqual(closest, gt)


def list_equals(a: List[Arbol], b: List[Arbol]) -> bool:
    """Devuelve True si todos los elementos de la lista a estan en b y todos los elementos de la lista b estan en a
    Se evalua igual que set(a) == set(b) si a y b fueran del tipo List[T] con T hasheable.
    """
    if len(a) != len(b):
        return False
    le = True
    for e in a:
        if e not in b:
            le = False
    for e in b:
        if e not in a:
            le = False
    return le


unittest.main()
