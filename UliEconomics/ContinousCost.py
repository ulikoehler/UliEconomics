#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd

def ConstantContinousCost(Cost):
    """
    Represents a cost that is continous and constant,
    i.e. every month the same cost, every year 12x the monthly cost etc.
    """
    def __init__(self, name, cost: float, per:pd.Timedelta|str="month"):
        if isinstance(per, str):
            # per="month" etc
            per = pd.Timedelta(1, unit=per)
        # Normalize cost to cost per second
        self.cost = cost / per.total_seconds()
    
    def is_continous(self) -> bool:
        return True
    
    def shift(self, num: float, unit: str) -> None:
        # For continous costs, the time shift has no effect
        pass
    
    def in_period(self, start: pd.Timestamp, end: pd.Timestamp) -> float:
        return self.cost * (end - start).total_seconds() / pd.Timedelta("1s").total_seconds()
    
    