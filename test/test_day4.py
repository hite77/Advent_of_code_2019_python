import unittest
from src.day4 import is_valid

# Going from left to right, the digits never decrease they increase or stay same
# (Like 111123 or 135679)
#
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


if __name__ == '__main__':
    unittest.main()
