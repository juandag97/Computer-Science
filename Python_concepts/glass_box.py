import unittest

def mayor_edad(edad):
    return True if edad >= 18 else False

class PruebaCristalTest(unittest.TestCase):

    def test_mayor(self):
        edad = 20

        resultado = mayor_edad(edad)

        self.assertEqual(resultado, True) 

    def test_menor(self):
        edad = 14
        resultado = mayor_edad(edad)
        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()