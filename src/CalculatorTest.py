import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_add_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_sub_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_mult_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 5), 10)
        self.assertEqual(calculator.result, 10)

    def test_divide_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.result, 5)

    def test_square_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.squaring(5), 25)
        self.assertEqual(calculator.result, 25)

    def test_sqrt_method(self):
        calculator = Calculator()
        self.assertEqual(calculator.takesqrroot(25), 5)
        self.assertEqual(calculator.result, 5)

if __name__ == '__main__':
    unittest.main()
