from functools import lru_cache

@lru_cache
def misma_paridad(n:int, m:int) -> bool:
    '''(100, 1):(22222222222, 2)'''
    return n%2 == m%2


@lru_cache
def alterna_paridad_(n:int) -> bool:
    '''(1010101010101):(20202022):(989898989898989899)'''
    #n_str:str = str(n)
    #digit_anterior:int = int(n_str[0])

    for i in range(1, len(n_str := (str(n)))):

       #digit:int = int(n_str[c])
        
        #if misma_paridad(digit, digit_anterior):
        #    return False
        if misma_paridad(int(n_str[i-1]), int(n_str[i])):
            return False
        
        #digit_anterior = digit

    return True

@lru_cache
def alterna_paridad(n:int) -> bool:
    '''(1010101010101):(20202022):(989898989898989899)'''
    alt:bool = True
    for i in range(1, len(str(n))):
        #alt *= not misma_paridad(int(str(n)[i-1]), int(str(n)[i]))
    	alt = alt and not misma_paridad(int(str(n)[i-1]), int(str(n)[i]))
    return alt

@lru_cache
def es_peculiar(n:int) -> bool:
    '''(705012):(505050500)'''
    return alterna_paridad(n) and n%22 == 0

@lru_cache
def n_esimo_peculiar(n:int) -> int:
    '''(100):(1000)'''
    cont:int = 0
    pos:int = 0
    while cont <= n:
        cont += 1 * es_peculiar(pos)
        pos += 1
    return pos-1

@lru_cache
def n_esimo_peculiar_(n:int) -> int:
    '''(100):(1000)'''
    segment:int = 0
    cant:int = 0
    while cant < n:
        cant += cant_peculiares_entre(segment, (segment := segment + 1))
    
    cont:int = 0
    for i in range(0, segment + 1):
        cont += 1 * es_peculiar(i)
        if cont == n+1:
            return i

@lru_cache
def n_esimo_peculiar__(n:int, _interval:int=1) -> int:
    segment:int = 0
    cant:int = 0
    while (cant := cant + cant_peculiares_entre(segment, (segment := segment + _interval))) < n:
        pass
    print(segment, segment + _interval + 1)
    print(cant)
    for i in range(segment, segment + _interval + 1):
        cant += 1 * es_peculiar(i)
        if cant == n:
            return i

@lru_cache
def n_peculiares(n:int) -> int:
    '''(1000):(4000)'''
    cont:int = 0
    pos:int = 0
    while cont <= n:
        if es_peculiar(pos):
            print(pos)
            cont += 1
        pos += 22
    return pos-22

@lru_cache
def cant_peculiares_entre(n:int, m:int) -> int:
    '''(100, 2000):(2000, 3000)'''
    cant:int = 0
    for i in range(n, m+1):
        cant += 1 * es_peculiar(i)
    return cant


def jaz_nesimo(pos):
	cant = 0
	aux = 0
	while cant<pos:
		aux+=1
		if (es_peculiar(aux)) == "si":
			cant += 1
	return aux



# Definir también las funciones auxiliares que se consideren necesarias.
