import unittest
from operacion_aritmeticas import OperacionesAritmeticas

class TestSuma(unittest.TestCase):

    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange

        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25
        objSuma = OperacionesAritmeticas(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas('a', 4)
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()


    def test_division_dosNumeros_retornaDivision(self):
        # Arrange

        operando1 = 6
        operando2 = 3
        resultadoEsperado = 2
        objDiv = OperacionesAritmeticas(operando1, operando2)

        # Act

        resultadoActual = objDiv.calcularDivision()

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        objDiv = OperacionesAritmeticas('a', 4)
        with self.assertRaises(TypeError):
            objDiv.calcularDivision()

    def test_division_operadorCero_lanzaExcepcion(self):
        objDiv = OperacionesAritmeticas(11, 0)
        with self.assertRaises(ZeroDivisionError):
            objDiv.calcularDivision()

if __name__ == '__main__':
    unittest.main()
