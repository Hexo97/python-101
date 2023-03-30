import unittest
from variables import *

class TestVariables(unittest.TestCase):

    def test_variable_declaration(self):
        self.assertEqual(name, "John")

    def test_variable_swap(self):
        self.assertEqual(num1, 20)
        self.assertEqual(num2, 10)

    def test_variable_types(self):
        self.assertEqual(a, 1)
        self.assertEqual(b, "Hello")
        self.assertEqual(c, True)

    def test_user_input(self):
        self.assertEqual(type(x), str)

    def test_list_append(self):
        self.assertEqual(my_list, [1, 2, 3, 4])

    def test_dictionary_access(self):
        self.assertEqual(my_dict["name"], "John")

if __name__ == '__main__':
    unittest.main()
