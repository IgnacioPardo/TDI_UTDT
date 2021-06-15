from tateti import Tateti
from pprint import pprint

t = Tateti()
print(t)
while not (w := t.jugada(input("Ingrese casillero: "))):
    print(t)

print(t)
print("Ganador ", w)
