import unittest
import one_hot_encoder


class TestEnc(unittest.TestCase):

    def test_double_city(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_unique_city(self):
        cities = ['Moscow', 'New York', 'Moscow']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 1]),
            ('New York', [1, 0]),
            ('Moscow', [0, 1]),
        ]
        self.assertEqual(actual, expected)

    def test_no_ny(self):
        cities = ['Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        self.assertNotIn(('New York', [0, 1]), actual)

    def test_exception(self):
        with self.assertRaises(Exception):
            one_hot_encoder.fit_transform()


if __name__ == '__main__':
    unittest.main()
