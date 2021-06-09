import unittest
from my_datetime import TimeZone


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class SampleTestCase(unittest.TestCase):

    def setUp(self):
        print('running setup')
        self.x = 100

    def tearDown(self):
        print('running tear down')

    def test_ok(self):
        self.x = 200
        self.assertEqual(200, self.x)

    def test_2(self):
        self.assertEqual(100, self.x)


class TestAccount(unittest.TestCase):

    def test_create_timezone(self):
        tz = TimeZone('Asia/Ho_Chi_Minh')
        self.assertEqual(tz.name, 'Asia/Ho_Chi_Minh')


run_tests(TestAccount)
