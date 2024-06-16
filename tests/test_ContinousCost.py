import unittest
from UliEconomics.ContinousCost import ConstantContinousCost
from UliEconomics.Interval import Interval
import pandas as pd

class TestConstantContinousCost(unittest.TestCase):
    def test_cost_in_interval(self):
        cost = ConstantContinousCost("Test Cost", 100, "month")
        interval = Interval(pd.Timestamp("2022-01-01"), pd.Timestamp("2022-02-01"))
        expected_cost = 100 * 24 * 60 * 60  # cost per second * number of seconds in the interval
        self.assertEqual(cost.cost_in_interval(interval), expected_cost)

    def test_monthly(self):
        cost = ConstantContinousCost("Test Cost", 100, "month")
        expected_monthly_cost = 100
        self.assertEqual(cost.monthly(), expected_monthly_cost)

    def test_yearly(self):
        cost = ConstantContinousCost("Test Cost", 100, "month")
        expected_yearly_cost = 100 * 12
        self.assertEqual(cost.yearly(), expected_yearly_cost)

    def test_multiply(self):
        cost = ConstantContinousCost("Test Cost", 100, "month")
        factor = 2
        expected_cost = 100 * factor
        multiplied_cost = cost * factor
        self.assertEqual(multiplied_cost.cost, expected_cost)

    def test_inplace_multiply(self):
        cost = ConstantContinousCost("Test Cost", 100, "month")
        factor = 2
        expected_cost = 100 * factor
        cost *= factor
        self.assertEqual(cost.cost, expected_cost)

if __name__ == "__main__":
    unittest.main()