import unittest
from src.day4 import is_valid, \
    numbers_increase_or_stay_same_from_left_to_right, \
    count_valid_for_range

# Secure container


class MyTestCase(unittest.TestCase):
    def test_duplicate_passes(self):
        self.assertEqual(True, is_valid(122345))

    def test_no_duplicate_digits_fails(self):
        self.assertEqual(False, is_valid(123456))

    def test_checking_for_increase_or_same_for_a_number(self):
        self.assertEqual(True, numbers_increase_or_stay_same_from_left_to_right(111123))
        self.assertEqual(True, numbers_increase_or_stay_same_from_left_to_right(135679))
        self.assertEqual(False, numbers_increase_or_stay_same_from_left_to_right(223450))

    def test_checking_for_valid_for_combined(self):
        self.assertEqual(True, is_valid(111111))
        self.assertEqual(False, is_valid(223450))
        self.assertEqual(False, is_valid(123789))
        self.assertEqual(False, is_valid(135679))

    def test_count_for_range_works(self):
        self.assertEqual(1, count_valid_for_range(111111, 111112))  # valid is 1000012

    def test_solution_for_my_range(self):
        self.assertEqual(1650, count_valid_for_range(178416, 676461))


if __name__ == '__main__':
    unittest.main()
