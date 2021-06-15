class Tateti:
    def __init__(self):
        self.tablero = list(range(0, 9))
        self.turno = 9

    def jugada(self, p: int):
        p = int(p)
        while p not in self.tablero:
            p = int(input("Ingrese otro casillero: "))
        self.tablero[int(p)] = self.turno
        if self.hay_ganador():
            return "x" if self.turno == 9 else "o"
        else:
            self.turno *= -1
            return False

    def hay_ganador(self):
        p = (
            [self.tablero[i : i + 3] for i in range(0, 9, 3)]
            + [
                [self.tablero[i], self.tablero[i + 3], self.tablero[i + 6]]
                for i in range(3)
            ]
            + [
                [self.tablero[0], self.tablero[4], self.tablero[8]],
                [self.tablero[2], self.tablero[4], self.tablero[6]],
            ]
        )
        return [self.turno] * 3 in p 

    def __repr__(self):
        return str(
            "\n".join(
                [
                    str(
                        [
                            "x" if f == 9 else "o" if f == -9 else f
                            for f in self.tablero
                        ][i : i + 3]
                    )
                    for i in range(0, 9, 3)
                ]
            )
        )
