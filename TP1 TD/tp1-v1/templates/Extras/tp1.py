import sys
from peculiar import es_peculiar, n_esimo_peculiar, cant_peculiares_entre,\
                     misma_paridad, alterna_paridad

## Acá va el código principal del programa, que
## invoca a las funciones requeridas.

if sys.argv[1] == "es_peculiar":
	if es_peculiar(sys.argv[2]):
		print("si")
	else:
		print("no")