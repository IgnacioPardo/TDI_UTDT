imports = "from peculiar import n_esimo_peculiar, n_esimo_peculiar_"

import timeit

amm = 1000
proms = [0] * amm
for n in range(0, 1000):
    for i in range(0, amm):
        proms[i] += (
            itter := timeit.timeit(
                stmt="n_esimo_peculiar_(" + str(i) + ")", setup=imports, number=1
            )
            / timeit.timeit(
                stmt="n_esimo_peculiar(" + str(i) + ")", setup=imports, number=1
            )
        ) / 1000
print(sum(proms) / len(proms))
"""
print("Peculiar nº100: while                 ", timeit.timeit(stmt="n_esimo_peculiar(100)", setup=imports, number=1))
print("Peculiar nº100: segmented (1)         ", timeit.timeit(stmt="n_esimo_peculiar_(100, 1)", setup=imports, number=1))
print("Peculiar nº100: segmented (10)        ", timeit.timeit(stmt="n_esimo_peculiar_(100, 10)", setup=imports, number=1))
print("Peculiar nº100: segmented (100)       ", timeit.timeit(stmt="n_esimo_peculiar_(100)", setup=imports, number=1))
print("Peculiar nº100: segmented (1000)      ", timeit.timeit(stmt="n_esimo_peculiar_(100, 1000)", setup=imports, number=1))
print("Peculiar nº100: segmented (10000)     ", timeit.timeit(stmt="n_esimo_peculiar_(100, 10000)", setup=imports, number=1))
print("")
print("Peculiar nº1000: while                ", timeit.timeit(stmt="n_esimo_peculiar(1000)", setup=imports, number=1))
print("Peculiar nº1000: segmented (1)        ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 1)", setup=imports, number=1))
print("Peculiar nº1000: segmented (10)       ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 10)", setup=imports, number=1))
print("Peculiar nº1000: segmented (100)      ", timeit.timeit(stmt="n_esimo_peculiar_(1000)", setup=imports, number=1))
print("Peculiar nº1000: segmented (1000)     ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 1000)", setup=imports, number=1))
print("Peculiar nº1000: segmented (10000)    ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 10000)", setup=imports, number=1))
print("Peculiar nº1000: segmented (100000)   ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 100000)", setup=imports, number=1))
print("Peculiar nº1000: segmented (1000000)  ", timeit.timeit(stmt="n_esimo_peculiar_(1000, 1000000)", setup=imports, number=1))
print("")
print("Peculiar nº5000: while                 ", timeit.timeit(stmt="n_esimo_peculiar(5000)", setup=imports, number=1))
print("Peculiar nº5000: segmented (1)         ", timeit.timeit(stmt="n_esimo_peculiar_(5000, 1)", setup=imports, number=1))
print("")
print("Peculiar nº10000: while               ", timeit.timeit(stmt="n_esimo_peculiar(10000)", setup=imports, number=1))
print("Peculiar nº10000: segmented (1)       ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 1)", setup=imports, number=1))
print("Peculiar nº10000: segmented (10)      ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 10)", setup=imports, number=1))
print("Peculiar nº10000: segmented (100)     ", timeit.timeit(stmt="n_esimo_peculiar_(10000)", setup=imports, number=1))
print("Peculiar nº10000: segmented (1000)    ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 1000)", setup=imports, number=1))
print("Peculiar nº10000: segmented (10000)   ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 10000)", setup=imports, number=1))
print("Peculiar nº10000: segmented (100000)  ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 100000)", setup=imports, number=1))
print("Peculiar nº10000: segmented (1000000) ", timeit.timeit(stmt="n_esimo_peculiar_(10000, 1000000)", setup=imports, number=1))

"""
"""
Peculiar nº100: while                  0.066702474
Peculiar nº100: segmented (1)          0.05387368500000002
Peculiar nº100: segmented (10)         0.143631532
Peculiar nº100: segmented (100)        0.145777948
Peculiar nº100: segmented (1000)       0.14247449500000003
Peculiar nº100: segmented (10000)      0.161482158

Peculiar nº1000: while                 2.437636801
Peculiar nº1000: segmented (1)         1.7446678979999999
Peculiar nº1000: segmented (10)        3.7382227499999994
Peculiar nº1000: segmented (100)       4.895253519000001
Peculiar nº1000: segmented (1000)      4.804534669000001
Peculiar nº1000: segmented (10000)     4.818308488
Peculiar nº1000: segmented (100000)    5.104164585000003
Peculiar nº1000: segmented (1000000)   5.804073539999997

Peculiar nº10000: while                54.438147963
Peculiar nº10000: segmented (1)        91.84778684800001
Peculiar nº10000: segmented (10)       91.10264149699998
Peculiar nº10000: segmented (100)      100.96236537200002
Peculiar nº10000: segmented (1000)     101.469510963
Peculiar nº10000: segmented (10000)    101.19884184199998
Peculiar nº10000: segmented (100000)   101.88789767399999
Peculiar nº10000: segmented (1000000)  105.21584391600004
"""
