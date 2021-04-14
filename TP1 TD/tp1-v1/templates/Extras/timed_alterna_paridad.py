imports = "from peculiar import alterna_paridad, alterna_paridad_"

import timeit

print("Alterna  111			", timeit.timeit(stmt="alterna_paridad(111)", setup=imports, number=1))
print("Alterna' 111			", timeit.timeit(stmt="alterna_paridad_(111)", setup=imports, number=1))
print("Alterna  121			", timeit.timeit(stmt="alterna_paridad(121)", setup=imports, number=1))
print("Alterna' 121			", timeit.timeit(stmt="alterna_paridad_(121)", setup=imports, number=1))
print("Alterna  2121212122		", timeit.timeit(stmt="alterna_paridad(2121212122)", setup=imports, number=1))
print("Alterna' 2121212122		", timeit.timeit(stmt="alterna_paridad_(2121212122)", setup=imports, number=1))
print("Alterna  989898989898989898989898989898989898989		", timeit.timeit(stmt="alterna_paridad(989898989898989898989898989898989898989)", setup=imports, number=1))
print("Alterna' 989898989898989898989898989898989898989		", timeit.timeit(stmt="alterna_paridad_(989898989898989898989898989898989898989)", setup=imports, number=1))