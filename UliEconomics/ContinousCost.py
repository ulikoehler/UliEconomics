#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd

class ConstantContinousCost(Cost):
    """
    Represents a cost that is continous and constant,
    i.e. every month the same cost, every year 12x the monthly cost etc.
    """
    def __init__(self, name, cost: float, per:pd.Timedelta|str="month", currency="€"):
        self.name = name
        self.currency = currency
        if isinstance(per, str):
            # per="month" etc
            per = pd.Timedelta(1, unit=per)
        # Store input arguments (more or less) for copying this instance
        self.cost = cost
        self.per = per
        # Normalize cost to cost per second (normalize to SI units)
        self.cost_per_second = cost / per.total_seconds()
    
    def is_continous(self) -> bool:
        return True
    
    def copy(self) -> "ConstantContinousCost":
        return ConstantContinousCost(self.name,
                                     cost=self.cost,
                                     per=self.per,
                                     currency=self.currency)
    
    def shift(self, timedelta: pd.Timedelta) -> None:
        # For continous costs, the time shift has no effect
        return self.copy()
    
    def in_period(self, start: pd.Timestamp, end: pd.Timestamp) -> float:
        return self.cost_per_second * (end - start).total_seconds() / pd.Timedelta("1s").total_seconds()
    
    def monthly(self) -> float:
        return self.cost_per_second * pd.Timedelta(1, "month").total_seconds() / pd.Timedelta("1s").total_seconds()
    
    def yearly(self) -> float:
        return self.cost_per_second * pd.Timedelta(1, "year").total_seconds() / pd.Timedelta("1s").total_seconds()
    
    def __mul__(self, other: float) -> "ConstantContinousCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.#
        """
        return ConstantContinousCost(
            name=self.name,
            cost=self.cost_per_second * other,
            per="second",
            currency=self.currency,
        )
        
    def __imul__(self, other: float) -> "ConstantContinousCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.
        This is the inplace version of __mul__.
        """
        self.cost_per_second *= other
        return self
    
    def __str__(self) -> str:
        return f"{self.monthly()} €/month"
    
    def __repr__(self) -> str:
        return f"ConstantContinousCost({self.__str__()})"