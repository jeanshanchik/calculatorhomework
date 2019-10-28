import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/test_subtraction.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )


if __name__ == '__main__':
    unittest.main()
