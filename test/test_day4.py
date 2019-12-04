import unittest
from src.day4 import is_valid, \
    numbers_increase_or_stay_same_from_left_to_right

# -111111 meets criteria (double 11, never decreases)
# -223450 does not decreasing 5 to 0
# -123789 no double
#
# How many different passwords in range meet this
#
# 178416-676461
#
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

# need to test for one of the above that is not decreasing for no duplicate to make sure it checks both

if __name__ == '__main__':
    unittest.main()
