import unittest
from code import *


class TestFixtures(unittest.TestCase):
    def test_isnotnone(self):
        self.assertIsNotNone(val, "Argumnet should not be none")

    def test_isnone(self):
        self.assertIsNone(foo, "Argumnet should be none")

    def test_isinstance(self):
        # self.assertIsInstance(a, Add)
        # self.assertIsInstance(m, Add)
        self.assertIsInstance(m, Multiply)

    def test_isnotinstance(self):
        self.assertNotIsInstance(m, Add)
        self.assertNotIsInstance(a, Multiply)


class Test_Almost(unittest.TestCase):
    def test_AlmostEqual(self):
        pass
        #  round(a-b, 2) == 0
        # 0.1 == 0 # fails
        # self.assertAlmostEqual(a, b, place=0)

    def test_NotAlmostEqual(self):
        self.assertNotAlmostEqual(a, b)


class Test_Exceptio(unittest.TestCase):
    def test_exceptionfun(self):
        self.assertNotRaises(ZeroDivisionError, fun, 40, 0)


if __name__ == "__main__":
    unittest.main()
