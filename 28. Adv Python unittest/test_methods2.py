import methods
import unittest


class Tests2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(methods2.add(10, 5), 15)
        self.assertEqual(methods2.add(1, -1), 0)
        self.assertEqual(methods2.add(-1, -1), -2)

    # def test_sub(self):
    #     self.assertEqual(methods2.sub(10, 5), 5)
    #     self.assertEqual(methods2.sub(1, -1), 2)
    #     self.assertEqual(methods2.sub(-1, -1), 0)

    # def test_multiply(self):
    #     self.assertEqual(methods2.multiply(10, 5), 50)
    #     self.assertEqual(methods2.multiply(1, -1), -1)
    #     self.assertEqual(methods2.multiply(-1, -1), 1)

    def test_division(self):
        self.assertEqual(methods2.division(10, 5), 2)
        self.assertEqual(methods2.division(1, -1), -1)
        self.assertEqual(methods2.division(-1, -1), 1)
        self.assertRaises(ValueError, methods2.division, 10, 0)

    def test_DatatypeEqual(self):
        self.assertTupleEqual((1, 2, 3, 4), (1, 2, 3, 4))
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertDictEqual({1: "a", 2: "b"}, {1: "a", 2: "b"})
        self.assertSetEqual({1, 2, 3, 4}, {1, 2, 3, 4})
        self.assertSequenceEqual({1, 2, 3, 4}, {1, 2, 3, 4})

    def test_boolEq(self):
        self.assertTrue(methods2.boolEq(10))

    def test_boolNot(self):
        self.assertFalse(methods2.boolNot(0))

    def test_TestIn(self):
        self.assertIn(methods2.TestIn(10), [10, 20, 30, 40])

    def test_GreaterEqual(self):
        self.assertGreaterEqual(methods2.GreaterEqual(50), 50)

    def test_equalList(self):
        self.assertListEqual([1, 2, 3, 4], [1, 2, 3, 4])

    def test_StringsTrue(self):
        self.assertTrue(methods2.foo.isupper())
        self.assertFalse(methods2.string.isupper())
        self.assertEqual(methods2.string.upper(), "PENAN")
        self.assertAlmostEqual(methods2.bar.split(), ["Hello", "World"])

    def test_split(self):
        pass


# new class means group of checks to be performed at once
class MembershipCheck(unittest.TestCase):
    # Use assertIn() to test container membership.
    def test_assertDict(self):

        self.assertIn(4, {1: "a", 4: "e"})

    def test_List(self):
        self.assertIn(4, [1, 2, 3, 4])

    def test_set(self):
        self.assertIn(4, set([1, 2, 3, 4]))


# Testing for Exceptions
class Test_Exception(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()

