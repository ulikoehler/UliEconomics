import unittest
from pandas import Timestamp
from UliEconomics.OneTimeCost import OneTimeCost
from UliEconomics.Interval import Interval
import pandas as pd

class TestOneTimeCost(unittest.TestCase):
    def test_is_continous(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        self.assertFalse(cost.is_continous())

    def test_copy(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        copy_cost = cost.copy()
        self.assertEqual(cost.name, copy_cost.name)
        self.assertEqual(cost.cost, copy_cost.cost)
        self.assertEqual(cost.currency, copy_cost.currency)
        self.assertEqual(cost.timepoint, copy_cost.timepoint)

    def test_shift(self):
        original_cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        shifted_cost = original_cost.shift(pd.Timedelta(days=1))
        self.assertEqual(shifted_cost.timepoint, Timestamp("2022-01-02"))
        # Check copy semantics
        self.assertEqual(original_cost.timepoint, Timestamp("2022-01-01"))

    def test_cost_in_interval(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        interval = Interval(Timestamp("2021-12-01"), Timestamp("2022-02-01"))
        self.assertEqual(cost.cost_in_interval(interval), 100)
        interval = Interval(Timestamp("2022-02-01"), Timestamp("2022-03-01"))
        self.assertEqual(cost.cost_in_interval(interval), 0)

    def test_multiply(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        multiplied_cost = cost * 2
        self.assertEqual(multiplied_cost.cost, 200)

    def test_imultiply(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        cost *= 2
        self.assertEqual(cost.cost, 200)

    def test_str(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        # No exact format string requirements, just check that the important info is present
        self.assertIn("100.00 €", str(cost))
        self.assertIn("2022-01-01", str(cost))

    def test_repr(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        self.assertIn("100.00 €", repr(cost))
        self.assertIn("2022-01-01", repr(cost))

    def test_sub_costs(self):
        cost = OneTimeCost("Test Cost", 100, Timestamp("2022-01-01"))
        sub_costs = cost.sub_costs()
        self.assertEqual(sub_costs, [])

if __name__ == "__main__":
    unittest.main()