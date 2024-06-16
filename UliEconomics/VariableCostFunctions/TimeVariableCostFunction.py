#!/usr/bin/env python3
from ..Cost import Cost
import pandas as pd
from ..Interval import Interval
from abc import ABC, abstractmethod

class TimeVariableCostFunction(ABC):
    """
    Represents a function to increase cost based only on time
    The increase is modeled as a multiplicative function.
    
    If the function returns 1.0, the cost stays the same
    If the function return <1.0, the resulting cost will be decreased
    If the function return >1.0, the resulting cost will be increased
    """
    @abstractmethod
    def cost_factor(self, timestamp: pd.Timestamp) -> float:
        """
        Return the cost factor for the given timestamp
        
        If the function returns 1.0, the cost stays the same
        If the function return <1.0, the resulting cost will be decreased
        If the function return >1.0, the resulting cost will be increased
        """
        raise NotImplementedError()