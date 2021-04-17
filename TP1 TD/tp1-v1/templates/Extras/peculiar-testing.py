import unittest

# Importamos el codigo a testear.
from peculiar import alterna_paridad_

#####################################################################


class TestAlternaParidad(unittest.TestCase):
    def test_unico_digito(self):
        self.assertTrue(alterna_paridad_(0))
        self.assertTrue(alterna_paridad_(1))

    def test_digitos_alternados(self):
        self.assertTrue(alterna_paridad_(12))
        self.assertTrue(alterna_paridad_(812))

    def test_digitos_consecutivos(self):
        self.assertFalse(alterna_paridad_(128))
        self.assertFalse(alterna_paridad_(821))
        self.assertFalse(alterna_paridad_(222))


## y así con el resto de las funciones a testear.

unittest.main()
