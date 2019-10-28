import unittest
from Calculator import Calculator
from CSVReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('./src/test_subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data = CsvReader('./src/test_addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply(self):
        test_data = CsvReader('./src/test_multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('./src/test_division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(int(row['Value 1']), int(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        test_data = CsvReader('./src/test_square.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.squaring(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('./src/test_square_root.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertAlmostEqual(self.calculator.sqrt(int(row['Value 1'])), float(row['Result']), places=4)
            self.assertAlmostEqual(self.calculator.result, float(row['Result']), places=4)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
