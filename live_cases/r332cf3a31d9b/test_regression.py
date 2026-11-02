import unittest
from live_cases.r332cf3a31d9b.duration import days_to_seconds


class DaysToSecondsRegression(unittest.TestCase):
    def test_one_day(self):
        self.assertEqual(days_to_seconds(1), 86400)

    def test_two_days(self):
        self.assertEqual(days_to_seconds(2), 172800)

    def test_seven_days(self):
        self.assertEqual(days_to_seconds(7), 604800)

    def test_zero(self):
        self.assertEqual(days_to_seconds(0), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            days_to_seconds(-1)

    def test_boolean_raises(self):
        with self.assertRaises(ValueError):
            days_to_seconds(True)
        with self.assertRaises(ValueError):
            days_to_seconds(False)

    def test_float_raises(self):
        with self.assertRaises(ValueError):
            days_to_seconds(1.5)

    def test_string_raises(self):
        with self.assertRaises(ValueError):
            days_to_seconds("1")


if __name__ == "__main__":
    unittest.main()
