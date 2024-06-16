#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd

class OneTimeCost(Cost):
    """
    Represents a cost which occurs exactly once at a specific point in time,
    with the entire cost being transferred instantly.
    """
    def __init__(self, name, cost: float, timepoint: pd.Timestamp, currency="€"):
        self.name = name
        self.cost = cost
        self.currency = currency
        self.timepoint = timepoint
    
    def is_continous(self) -> bool:
        return False
    
    def copy(self) -> "OneTimeCost":
        return OneTimeCost(self.name,
                           cost=self.cost,
                           timepoint=self.timepoint,
                           currency=self.currency)
    
    def shift(self, timedelta: pd.Timedelta) -> None:
        # For continous costs, the time shift has no effect
        return OneTimeCost(
            self.name,
            cost=self.cost,
            timepoint=self.timepoint + timedelta,
            currency=self.currency
        )
    
    def in_period(self, start: pd.Timestamp, end: pd.Timestamp) -> float:
        if self.timepoint >= start and self.timepoint < end:
            return self.cost
        else: # timepoint is outside interval
            return 0
    
    def __mul__(self, other: float) -> "OneTimeCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.#
        """
        return OneTimeCost(
            name=self.name,
            cost=self.cost * other,
            timepoint=self.timepoint,
            currency=self.currency,
        )
        
    def __imul__(self, other: float) -> "OneTimeCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.
        This is the inplace version of __mul__.
        """
        self.cost *= other
        return self
    
    def __str__(self) -> str:
        return f"{self.cost:.2f} € @ {self.timepoint}"
    
    def __repr__(self) -> str:
        return f"OneTimeCost({self.__str__()})"