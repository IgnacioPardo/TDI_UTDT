import unittest

# Importamos el codigo a testear.
from peculiar import (
    es_peculiar,
    n_esimo_peculiar,
    cant_peculiares_entre,
    misma_paridad,
    alterna_paridad,
)


class TestMismaParidad(unittest.TestCase):
    def test_ceros(self):
        self.assertTrue(misma_paridad(0, 0))

    def test_cero_impar(self):
        self.assertFalse(misma_paridad(0, 3))
        self.assertFalse(misma_paridad(3, 0))

    def test_pares(self):
        self.assertTrue(misma_paridad(2, 4))
        self.assertTrue(misma_paridad(4, 2))

    def test_impares(self):
        self.assertTrue(misma_paridad(5, 9))
        self.assertTrue(misma_paridad(9, 5))

    def test_diferentes(self):
        self.assertFalse(misma_paridad(7, 8))


class TestAlternaParidad(unittest.TestCase):
    def test_unico_digito(self):
        self.assertTrue(alterna_paridad(0))
        self.assertTrue(alterna_paridad(1))

    def test_digitos_alternados(self):
        self.assertTrue(alterna_paridad(12))
        self.assertTrue(alterna_paridad(812))

    def test_digitos_consecutivos(self):
        self.assertFalse(alterna_paridad(128))
        self.assertFalse(alterna_paridad(821))
        self.assertFalse(alterna_paridad(222))


class TestEsPeculiar(unittest.TestCase):
    def test_numeros_peculiares(self):
        self.assertTrue(es_peculiar(0))
        self.assertTrue(es_peculiar(418))
        self.assertTrue(es_peculiar(616))
        self.assertTrue(es_peculiar(638))
        self.assertTrue(es_peculiar(814))
        self.assertTrue(es_peculiar(836))
        self.assertTrue(es_peculiar(858))
        self.assertTrue(es_peculiar(1012))
        self.assertTrue(es_peculiar(1034))
        self.assertTrue(es_peculiar(1056))
        self.assertTrue(es_peculiar(1078))

    def test_numeros_no_peculiares(self):
        self.assertFalse(es_peculiar(1))
        self.assertFalse(es_peculiar(428))
        self.assertFalse(es_peculiar(626))
        self.assertFalse(es_peculiar(648))
        self.assertFalse(es_peculiar(824))
        self.assertFalse(es_peculiar(846))
        self.assertFalse(es_peculiar(868))
        self.assertFalse(es_peculiar(1038))
        self.assertFalse(es_peculiar(1054))
        self.assertFalse(es_peculiar(1111))
        self.assertFalse(es_peculiar(1334))


class TestEnesimoPeculiar(unittest.TestCase):
    def test_n_esimo_peculiar(self):
        self.assertEqual(n_esimo_peculiar(0), 0)
        self.assertEqual(n_esimo_peculiar(1), 418)
        self.assertEqual(n_esimo_peculiar(2), 616)
        self.assertEqual(n_esimo_peculiar(3), 638)
        self.assertEqual(n_esimo_peculiar(4), 814)


class TestCantidadPeculiaresentre(unittest.TestCase):
    def test_cantidad_correcta_en_intervalo(self):
        self.assertEqual(cant_peculiares_entre(0, 0), 1)
        self.assertEqual(cant_peculiares_entre(0, 1), 1)
        self.assertEqual(cant_peculiares_entre(1, 12), 0)
        self.assertEqual(cant_peculiares_entre(0, 400), 1)
        self.assertEqual(cant_peculiares_entre(0, 500), 2)
        self.assertEqual(cant_peculiares_entre(1000, 2000), 18)
        self.assertEqual(cant_peculiares_entre(2000, 3000), 0)


unittest.main()
