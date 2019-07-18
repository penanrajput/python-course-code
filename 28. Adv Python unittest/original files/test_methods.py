import methods
import unittest


class Tests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(methods.add(10, 5), 15)
        self.assertEqual(methods.add(1, -1), 0)
        self.assertEqual(methods.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(methods.sub(10, 5), 5)
        self.assertEqual(methods.sub(1, -1), 2)
        self.assertEqual(methods.sub(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(methods.multiply(10, 5), 50)
        self.assertEqual(methods.multiply(1, -1), -1)
        self.assertEqual(methods.multiply(-1, -1), 1)

    def test_division(self):
        self.assertEqual(methods.division(10, 5), 2)
        self.assertEqual(methods.division(1, -1), -1)
        self.assertEqual(methods.division(-1, -1), 1)


if __name__ == "__main__":
    unittest.main()

