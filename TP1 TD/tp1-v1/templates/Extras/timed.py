not_include = set(locals().keys())

from peculiar import (
    es_peculiar,
    n_esimo_peculiar,
    cant_peculiares_entre,
    misma_paridad,
    alterna_paridad,
    alterna_paridad_,
    n_esimo_peculiar_,
)

include = set(globals().keys())
funcs = include.difference(not_include.union({"not_include"}))

imports = "from peculiar import es_peculiar, n_esimo_peculiar, cant_peculiares_entre, misma_paridad, alterna_paridad, alterna_paridad_, n_esimo_peculiar_"

import timeit

for func in funcs:
    for params in globals()[func].__doc__.split(":"):
        print(
            func + params,
            timeit.timeit(
                stmt=func + params, setup="from peculiar import " + func, number=1
            ),
        )
    print()

"""
print("100: while", timeit.timeit(stmt="n_esimo_peculiar(100)", setup=imports, number=1))
print("100: segmented (1)", timeit.timeit(stmt="n_esimo_peculiar_(100, 1)", setup=imports, number=1))
print("100: segmented (10)", timeit.timeit(stmt="n_esimo_peculiar_(100, 10)", setup=imports, number=1))
print("100: segmented (100)", timeit.timeit(stmt="n_esimo_peculiar_(100)", setup=imports, number=1))
print("100: segmented (1000)", timeit.timeit(stmt="n_esimo_peculiar_(100, 1000)", setup=imports, number=1))
print("100: segmented (10000)", timeit.timeit(stmt="n_esimo_peculiar_(100, 10000)", setup=imports, number=1))
print("")
print("1000: while", timeit.timeit(stmt="n_esimo_peculiar(1000)", setup=imports, number=1))
print("1000: segmented (1)", timeit.timeit(stmt="n_esimo_peculiar_(1000, 1)", setup=imports, number=1))
print("1000: segmented (10)", timeit.timeit(stmt="n_esimo_peculiar_(1000, 10)", setup=imports, number=1))
print("1000: segmented (100)", timeit.timeit(stmt="n_esimo_peculiar_(1000)", setup=imports, number=1))
print("1000: segmented (1000)", timeit.timeit(stmt="n_esimo_peculiar_(1000, 1000)", setup=imports, number=1))
print("1000: segmented (10000)", timeit.timeit(stmt="n_esimo_peculiar_(1000, 10000)", setup=imports, number=1))
"""
