def paridad(x:int) -> int: 
	"""
		Dado un entero x devuelve 0(cero) si x es par y 1(uno) en caso contrario.
		Precondicion: x es un entero
		Postcondicion: 	vr = 0 si x es par 
						vr = 1 si x no es par
	"""

	vr:int = x%2
	return vr