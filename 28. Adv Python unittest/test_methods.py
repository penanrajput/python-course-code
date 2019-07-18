import unittest
from methods import *

# https://pymotw.com/3/unittest/


class Test_Arithmatic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 6), 10)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 6), -2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(-1, 1), -2)

    def test_division(self):
        print("In Test_division function")
        self.assertEqual(division(10, 5), 2)
        self.assertEqual(division(-1, -1), 1.0)
        self.assertEqual(division(-1, 1), -1.0)
        self.assertRaises(ValueError, division, 2, 0)


class Test_Exception(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(ValueError, division, 20, 0)
        self.assertRaises(SyntaxError)


class Test_Regex(unittest.TestCase):
    def test_regex(self):
        self.assertRegex("abc", "a")
        self.assertRegex("abc", "b")
        # The next assertions are not verified!
        # self.assertRegex("abc", "d")
        # self.assertRegex('abc', 'e')
        self.assertRegex(email, r"\w+@gmail.com")


class Test_SkippingTest(unittest.TestCase):
    def test_skip(self):
        pass

    def test_skipTest(self):
        raise unittest.SkipTest("skipping via exception")


class Test_skippingDecorators(unittest.TestCase):
    @unittest.skipIf(6 > 4, "Skip Over this routine")
    def test_skipped(self):
        self.assertEqual(4, 6)

    @unittest.skipUnless(b == 10, "Skip Unless b == 20")
    # when b is 10, test is skipped
    def test_skipunless(self):
        self.assertNotEqual(a + b, 20)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(a * b, 100)

    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_always_passes(self):
        self.assertTrue(True)

    @classmethod
    def setUpClass(cls):
        print("called once before any tests in Test_skippingDecorators class")

    @classmethod
    def tearDownClass(cls):
        print("\ncalled once after all tests in Test_skippingDecorators class")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # unittest.main(verbosity=2).run(suite)

