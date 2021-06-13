from arbol import Arbol
from typing import Set, List, Dict, TextIO
import csv


class DataSetArboreo:
    def __init__(self, filename: str):
        """Descripcion: DataSet de objetos de la clase Arbol a partir de los registros un archivo CSV (filename).
        Precondicion: filename es un path de tipo str a un archivo CSV, que contenga valores al menos para los siguientes campos:
                "long", "lat", "id_arbol", "nombre_cie", "barrio", "calle", "chapa1"
        """
        self._arboles: List[Arbol] = []
        self._size: int = 0
        self._barrios: Set[str] = set()
        self._especies: Set[str] = set()

        f: TextIO = open(filename, encoding="utf-8")
        a: Dict[str, str]
        for a in csv.DictReader(f):
            self._arboles.append(
                Arbol(
                    float(a["long"]),
                    float(a["lat"]),
                    a["id_arbol"],
                    a["nombre_cie"],
                    a["barrio"],
                    a["calle"],
                    a["chapa1"],
                )
            )
            self._size += 1
            self._barrios.add(a["barrio"])
            self._especies.add(a["nombre_cie"])
        f.close()

    def tamano(self) -> int:
        """Descripcion: Devuelve la cantidad de árboles en el DataSet.
        Precondicion:
        Postcondicion: Un valor numerico natural o 0 en funcion a la cantidad de Arboles en el DataSet.
        """
        return self._size

    def especies(self) -> Set[str]:
        """Descripcion: Devuelve las especies de los árboles del DataSet.
        Precondicion:
        Postcondicion: Un conjunto conteniendo a todas las especies presentes en la propiedad especie de los objetos Arbol del DataSet
        """
        return self._especies

    def barrios(self) -> Set[str]:
        """Descripcion: Devuelve el conjunto de barrios de los árboles del DataSet.
        Precondicion:
        Postcondicion: Un conjunto conteniendo a todas los barrios presentes en la propiedad barrio de los objetos Arbol del DataSet
        """
        return self._barrios

    def arboles_de_la_especie(self, especie: str) -> List[Arbol]:
        """Descripcion: Devuelve los árboles del DataSet que tienen la especie indicada.
        Precondicion: Especie es un valor de tipo str descriptivo de una especie de árbol existente.
        Postcondicion: Una lista conteniendo a los Arbol del DataSet cuya propiedad especie se la misma a la indicada por parametro.
        """
        return [a for a in self._arboles if a.especie == especie]

    def cantidad_por_especie(self, minimo: int) -> Dict[str, int]:
        """Descripcion: Devuelve un diccionario que indica la cantidad de ejemplares de cada especie existente en el DataSet, pero incluyendo solamente a las especies que tienen como mínimo la cantidad de ejemplares indicada.
        Precondicion: minimo es un numero entero no negativo.
        Postcondicion: Un diccionario donde las keys son las especies correspondientes a una clave numerica cantidad, cuyo valor es mayor o igual al valor indicado como minimo.
        """
        vr: Dict[str, int] = dict()
        e: str
        for e in self.especies():
            c: int = len(self.arboles_de_la_especie(e))
            if c > minimo:
                vr[e] = c

        return vr

    def arbol_mas_cercano(self, especie: str, lat: float, lng: float) -> Arbol:
        """Descripcion: Devuelve el árbol de la especie indicada que está más cercano al punto ⟨lat, lng⟩ en el DataSet, usando la distancia euclidiana.
        Precondicion: Existe al menos un Arbol de la especie indicada en el DataSet.
        Postcondicion: El árbol de la especie indicada que está más cercano al punto ⟨lat, lng⟩ en el DataSet.
        """
        vr: Arbol = self.arboles_de_la_especie(especie)[0]
        min_d: int = vr.distancia(lat, lng)
        a: Arbol
        for a in self._arboles:
            if a.especie == especie:
                d: int = a.distancia(lat, lng)
                if not min_d:
                    min_d = d
                    vr = a
                else:
                    if d < min_d:
                        min_d = d
                        vr = a
        return vr

    def __repr__(self):
        return str(self._arboles)
