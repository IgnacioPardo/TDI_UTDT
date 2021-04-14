import sys
from peculiar import es_peculiar, n_esimo_peculiar, cant_peculiares_entre, misma_paridad, alterna_paridad

## Acá va el código principal del programa, que
## invoca a las funciones requeridas.


def cli():
    nombre_funcion = sys.argv[1]
    if nombre_funcion == 'es_peculiar':
        n:int = int(sys.argv[2])
        if es_peculiar(n):
            print('sí')
        else:
            print('no')
    elif nombre_funcion == 'alterna_paridad':
        n:int = int(sys.argv[2])
        if alterna_paridad(n):
            print('sí')
        else:
            print('no')
    elif nombre_funcion == 'n_esimo_peculiar':
        n:int = int(sys.argv[2])
        print(n_esimo_peculiar(n))
    elif nombre_funcion == 'misma_paridad':
        n:int = int(sys.argv[2])
        m:int = int(sys.argv[3])
        if misma_paridad(n, m):
            print('sí')
        else:
            print('no')
    elif nombre_funcion == 'cant_peculiares_entre':
        n:int = int(sys.argv[2])
        m:int = int(sys.argv[3])
        print(cant_peculiares_entre(n, m))
    else:
      print("Funcion desconocida")
      quit()


class NegativoError(Exception):
		pass

def validate_param(n:str) -> int:
	# Descripcion: Valida el argumento pasado por consola para ser evaluado en alguna funcion, de ser parseable a int y mayor o igual a 0, se retorna un int de n, de lo contrario lanza una excepcion, informa al usuario el error y finaliza el programa.
	# Precondicion: n es cualquier string
	# Postcondicion: vr=int(n) si es valido, finaliza el programa de lo contrario
	try:
			if int(n) < 0:
				raise NegativoError("numero menor a 0: " + n)
	except Exception as e:
		print("Los parametros deben ser numeros enteros mayores o iguales que 0.")
		print("\t", e)
		quit()
	return int(n)

def cli_():
  if sys.argv[1] not in globals():
    print("Funcion desconocida")
    quit()

  print(res if not isinstance((res := globals()[sys.argv[1]](*[validate_param(n) for n in sys.argv[2:]])), bool) else "sí" if res else "no")
		
if __name__ == "__main__": 
	cli()
	#cli_()
