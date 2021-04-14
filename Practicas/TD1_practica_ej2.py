def suma_inversos(x:int, y:int) -> float:
	"""
	Retorna la suma de sus inversos
	Precondicion: x, y enteros distintos de 0
	Postcondicion: vr:float es la suma del inverso de x con el inverso de y (1/x + 1/y)
	"""
	return 1/x + 1/y

a:float = suma_inversos(1, 2) #1.5
b:float = suma_inversos(2, 4) #0.75
print(a, b)

def suma_inversos_(x :int, y : int) -> float:
	"""
	Retorna la suma de sus inversos
	Precondicion: x, y enteros distintos de 0
	Postcondicion: vr:float es la suma del inverso de x con el inverso de y (1/x + 1/y)

	y / (x*y) + (x*y) * x / (x*y)*(x*y)
	1 / x + (x**2 * y)  / (x**2 * y**2)
	1/x   +   1/y
	"""
	a : int = x * y
	b : int = a * a
	return y / a + a * x / b


c:float = suma_inversos_(1,2)
d:float = suma_inversos_(2,4)
print(c, d)
