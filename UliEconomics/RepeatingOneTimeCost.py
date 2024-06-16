#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd
from .Interval import Interval

class RepeatingOneTimeCost(Cost):
    """
    Represents a cost which occurs instantly at specific intervals.
    The cost occurs first at [timepoint] (no cost occurs before that)
    and repeats at [interval] ad infinitum.
    """
    def __init__(self, name, cost: float, timepoint: pd.Timestamp, interval: pd.Timedelta, currency="€"):
        self.name = name
        self.cost = cost
        self.currency = currency
        self.timepoint = timepoint
        self.interval = interval
    
    def is_continous(self) -> bool:
        return False
    
    def copy(self) -> "RepeatingOneTimeCost":
        return RepeatingOneTimeCost(self.name,
                           cost=self.cost,
                           timepoint=self.timepoint,
                           interval=self.interval,
                           currency=self.currency)
    
    def shift(self, timedelta: pd.Timedelta) -> None:
        # Only shifts the timepoint, interval stays the same.
        return RepeatingOneTimeCost(
            self.name,
            cost=self.cost,
            timepoint=self.timepoint + timedelta,
            interval=self.interval,
            currency=self.currency
        )

    def cost_in_interval(self, interval: Interval) -> float:
        if interval.end <= self.timepoint:
            # No cost occurs before timepoint
            return 0.0
        # Increase timestamp by [interval] until
        # it's in the interval
        cumulative_cost = 0.0
        current_timestamp = self.timepoint
        while current_timestamp < interval.end:
            if interval.includes(current_timestamp):
                cumulative_cost += interval
            current_timestamp += self.interval
        return cumulative_cost
        
    def __mul__(self, other: float) -> "RepeatingOneTimeCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.#
        """
        return RepeatingOneTimeCost(
            name=self.name,
            cost=self.cost * other,
            timepoint=self.timepoint,
            interval=self.interval,
            currency=self.currency,
        )
        
    def __imul__(self, other: float) -> "RepeatingOneTimeCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.
        This is the inplace version of __mul__.
        """
        self.cost *= other
        return self
    
    def __str__(self) -> str:
        return f"{self.cost:.2f} € every {self.interval} starting from {self.timepoint}"
    
    def __repr__(self) -> str:
        return f"IntervalCost({self.__str__()})"