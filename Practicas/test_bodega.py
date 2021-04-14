#Ejercicio de la clase practica n3

#NO ES NECESARIO QUE SEPAN CÓMO FUNCIONA nueva_bodega PERO SI QUÉ HACE

import unittest

def nueva_bodega(s:str) -> bool:
    vino:str = 'vino'
    bodega:str = 'bodega'
    nueva:str = 'nueva'
    
    s = s.lower()

    vr:bool = nueva in s or vino in s or bodega in s 
    return vr



#   ACA EMPIEZAN LOS TEST 

class TestNuevaBodega(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    
    def test_verdaderos(self):
        self.assertTrue(nueva_bodega('nueva bodega'))
        self.assertEqual(nueva_bodega('nuevas vinotecas abren en la ciudad, venga por su vino'), True)
        #NUEVO TEST

        self.assertTrue(nueva_bodega("En mi bodega tengo muchos vinos"))
        self.assertTrue(nueva_bodega("En mi casa no queda vino"))
        self.assertTrue(nueva_bodega("Mira mi nueva cartera"))
        self.assertTrue(nueva_bodega("El vino es una bebida obtenida de la uva, mediante la fermentación alcohólica de su mosto o zumo"))
        self.assertTrue(nueva_bodega("Bodega es lugar donde se elaboran y almacenan bebidas"))
        self.assertTrue(nueva_bodega("NUEVA BODEGA DE VINOS"))
        
        
    def test_falsos(self):
        self.assertFalse(nueva_bodega('tengo un nuevo libro en mi biblioteca'))
        #NUEVO TEST

        self.assertFalse(nueva_bodega("Hoy es viernes"))
        self.assertFalse(nueva_bodega("Bienvenidos a Introduccion a la Programacion"))
        self.assertFalse(nueva_bodega("2+2 = 4"))
        self.assertFalse(nueva_bodega("Hola como estas"))


# esta linea es para correr los test previamente declarados
unittest.main()
