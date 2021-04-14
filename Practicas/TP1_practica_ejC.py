def f(x:int, y:int) -> int:
	x = 10
	return x + y

b:int = 8
r:int = f(b, b)
print(r)

r=f(x,b)
print(r)