def misma_paridad(n: int, m: int) -> bool:
    """
    Descripcion:  La funcion evalúa si n y m son ambos pares o ambos impares.

    Precondicion: n y m deben ser números enteros mayores o iguales que 0.

    Postcondicion: El valor de retorno es una variable del tipo bool, con valor verdadero (True) si y solo si 1) n y m son ambos pares,  2) ambos numeros son impares. En caso contrario, la funcion devuelve un valor falso (False).
    """

    return n % 2 == m % 2


def alterna_paridad(n: int) -> bool:
    """
    Descripcion: Evalua si los digitos de n se alternan entre par e impar.

    Precondicion: n debe ser un número entero mayor o igual que 0.

    Postcondicion: El valor de retorno equivale a que los digitos de n alternan o no su paridad.
    """

    i: int = 1
    n_str: str = str(n)

    while i < len(n_str):
        if misma_paridad(int(n_str[i - 1]), int(n_str[i])):
            return False
        i += 1
    return True


def es_peculiar(n: int) -> bool:
    """
    Descripcion: Evalua si el numero ingresado es o no peculiar.

    Precondicion: n debe ser un número entero mayor o igual que 0.

    Postcondicion: Retorna un bool en funcion si n es o no un numero peculiar.
    """

    return alterna_paridad(n) and n % 22 == 0


def n_esimo_peculiar(n: int) -> int:
    """
    Descripcion: Retorna el n-esimo número peculiar.

    Precondicion: n debe ser un número entero mayor o igual que 0.

    Postcondicion: Retorna el n-esimo número peculiar.
    """

    cont: int = 0
    pos: int = 0
    while cont <= n:
        # cont += es_peculiar(i)
        if es_peculiar(pos):
            cont += 1
        pos += 22
    return pos - 22


def cant_peculiares_entre(n: int, m: int) -> int:
    """
    Descripcion: Calcula la cantidad de numeros pecularies entre n y m inclusives.

    Precondicion: n y m deben ser números enteros mayores o iguales que 0. m debe ser mayor o igual a n.

    Postcondicion: Retorna un entero representando la cantidad de numeros pecularies que existen entre n y m inclusives.
    """

    cant: int = 0
    i: int = n
    while i <= m:
        # cant += es_peculiar(i)
        if es_peculiar(i):
            cant += 1
        i += 1
    return cant
