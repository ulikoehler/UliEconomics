#!/usr/bin/env python3
from ..Cost import Cost
import pandas as pd
from ..Interval import Interval
from .TimeVariableCostFunction import TimeVariableCostFunction

class LinearTimeVariableCostFunction(TimeVariableCostFunction):
    """
    Represents a function that linearly increases the cost factor,
    based on how much time has passed since a time point t0.
    
    Before, t0, the cost is decreased linearly.
    """
    def __init__(self, t0: pd.Timestamp, increase_factor: float, per=pd.Timedelta):
        self.t0 = t0
        # Compute additive cost per second since t0
        self.factor_per_second = self.increase / per.total_seconds()
        # Save original inputs for __str__() etc
        self.increase_factor = increase_factor
        self.per = per
    
    def cost_factor(self, timestamp: pd.Timestamp) -> float:
        """
        Return the cost factor for the given timestamp
        
        If the function returns 1.0, the cost stays the same
        If the function return <1.0, the resulting cost will be decreased
        If the function return >1.0, the resulting cost will be increased
        """
        time_since_t0 = (timestamp - self.t0).total_seconds
        return 1.0 + self.factor_per_second()

    def 