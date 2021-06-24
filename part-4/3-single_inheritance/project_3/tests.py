from project_3 import CPU
from unittest import TestCase, TestLoader, TextTestRunner


def run_tests(test_class):
    suite = TestLoader().loadTestsFromTestCase(test_class)
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


class CPUTestCase(TestCase):

    def setUp(self) -> None:
        self.cpu1 = CPU('Intel-Core-I9', 10, 'Intel', 4, 5, 20)
        self.cpu2 = CPU('AMD-R123', 11, 'AMD', 8, 16, 20)

    def test_create_instance_successfully(self):
        self.assertEqual(self.cpu1.name, 'Intel-Core-I9')
        self.assertEqual(self.cpu1.total, 10)
        self.assertEqual(self.cpu1.allocated, 0)

        self.assertEqual(self.cpu2.manufacturer, 'AMD')

    def test_create_instance_bad_value_string(self):
        with self.assertRaises(ValueError):
            cpu3 = CPU('Intel-Core-I9', '10', 'Intel', 4, 5, 20)

    def test_create_instance_bad_value_value_less_than_0(self):
        with self.assertRaises(ValueError):
            cpu3 = CPU('Intel-Core-I9', 10, 'Intel', 4, 5, 20, allocated=-2)

    def test_claim_cpu_successfully(self):
        self.cpu1.claim(2)

        self.assertEqual(self.cpu1.total, 10)
        self.assertEqual(self.cpu1.allocated, 2)

    def test_claim_cpu_value_bigger_than_allocated(self):
        with self.assertRaises(ValueError):
            self.cpu1.claim(11)
        self.assertEqual(self.cpu1.allocated, 0)

    def test_freeup_cpu_successfully(self):
        self.cpu1.claim(2)
        self.cpu1.freeup(2)

        self.assertEqual(self.cpu1.allocated, 0)
        self.assertEqual(self.cpu1.total, 10)

    def test_freeup_cpu_value_bigger_than_allocated(self):
        self.cpu1.claim(2)
        with self.assertRaises(ValueError):
            self.cpu1.freeup(4)

        self.assertEqual(self.cpu1.allocated, 2)
        self.assertEqual(self.cpu1.total, 10)

    def test_died_cpu_successfully(self):
        self.cpu1.claim(4)
        self.cpu1.died(2)

        self.assertEqual(self.cpu1.allocated, 2)
        self.assertEqual(self.cpu1.total, 8)

    def test_died_cpu_value_bigger_than_allocated(self):
        self.cpu1.claim(4)
        with self.assertRaises(ValueError):
            self.cpu1.died(5)

    def test_died_cpu_allocated_equal_0(self):
        with self.assertRaises(ValueError):
            self.cpu1.died(5)

    def test_category(self):
        self.assertEqual(self.cpu1.category, 'cpu')


run_tests(CPUTestCase)
