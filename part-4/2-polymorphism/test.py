from project import Mod
from unittest import TestCase, TestLoader, TextTestRunner


def run_tests(test_class):
    suite = TestLoader().loadTestsFromTestCase(test_class)
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


class ModTestCase(TestCase):

    def setUp(self) -> None:
        self.m1 = Mod(8, 12)
        self.m2 = Mod(20, 12)
        self.m3 = Mod(7, 12)
        self.m4 = Mod(8, 13)

    def test_add_successfully(self):
        result = self.m1 + self.m2
        self.assertEqual(result, 16)

    def test_compare_less_than_success(self):
        self.assertTrue(self.m3 < self.m1)

    def test_incompatible_checking(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(self.m1, self.m3)


run_tests(ModTestCase)
