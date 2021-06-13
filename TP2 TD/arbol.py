class Arbol:
    def __init__(
        self,
        long: float,
        lat: float,
        id_: str,
        especie: str,
        barrio: str,
        calle: str,
        num: str,
    ):
        """Inicializa Arbol con sus respectivos atributos
        Precondicion: ninguna
        Postcondicion: arbol tiene latitud = lat, longitud = long, especie = especie,
        barrio = barrio, direccion = direccion
        """

        self.lat: float = lat
        self.long: float = long
        self.id: str = id_
        self.especie: str = especie
        self.barrio: str = barrio
        self.direccion: str = calle + " " + num

    def distancia(self, lat: float, long: float) -> float:
        """Devuelve la distancia euclidiana entre self? y el punto P(lat, long)
        Precondicion: ninguna
        Postcondicion: vr es igual a la raiz de las diferencia de latitudes al cuadrado, mas la diferencia de longitudes al cuadrado de self y lat y long.
        """

        vr: float = 0
        dif_x: float = (self.lat - lat) ** 2
        dif_y: float = (self.long - long) ** 2

        vr = (dif_x + dif_y) ** 0.5

        return vr

    def __eq__(self, other):
        """Devuelve la comparacion igualdad entre el mismo objeto y otro dado"""
        if isinstance(other, Arbol):
            return (
                self.lat == other.lat
                and self.long == other.long
                and self.id == other.id
                and self.especie == other.especie
                and self.barrio == other.barrio
                and self.direccion == other.direccion
            )
        return False

    def __repr__(self):
        """Devuelve la representacion de string de Arbol
        La representacion consiste en el id de self
        """
        return self.id
