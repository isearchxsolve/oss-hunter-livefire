import unittest
from live_cases.r33c5cf9b171f.duration import days_to_seconds

class Baseline(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(days_to_seconds(0), 0)
    def test_negative(self):
        with self.assertRaises(ValueError):
            days_to_seconds(-1)
