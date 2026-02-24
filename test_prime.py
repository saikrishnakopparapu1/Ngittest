import unittest
import prime


class TestGetOdds(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(prime.get_odds([]), [])

    def test_all_odds(self):
        data = [1, 3, 5, 7]
        self.assertEqual(prime.get_odds(data), data)

    def test_mixed_numbers(self):
        self.assertEqual(prime.get_odds([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_non_integers(self):
        self.assertEqual(prime.get_odds([1, 2.5, 3, '5', 7]), [1, 3, 7])

    def test_negative_and_zero(self):
        self.assertEqual(prime.get_odds([-3, -2, 0, 1]), [-3, 1])


if __name__ == "__main__":
    unittest.main()
