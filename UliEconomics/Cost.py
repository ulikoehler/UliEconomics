#!/usr/bin/env python3
from abc import ABC, abstractmethod
import pandas as pd
from .Interval import Interval
from typing import List

class Cost(ABC):
    
    @abstractmethod
    def cost_in_interval(self, interval: Interval) -> float:
        """
        Get the sum of account changes from this cost in the period
        from [start, end).
        """
        raise NotImplementedError()
    
    @abstractmethod
    def is_continous(self) -> bool:
        """
        Return true if this cost can be linearly
        distributed onto any period.
        
        Note that piecewise continous costs are not continous.
        """
        raise NotImplementedError()
    
    @abstractmethod
    def shift(self, timedelta: pd.Timedelta) -> "Cost":
        """
        Shift this cost by a given timedelta.
        Positive timedeltas shift to the future.
        Negative timedeltas shift to the past.
        
        Does not modify the current instance but creates a new instance
        """
        raise NotImplementedError()
    
    @abstractmethod
    def sub_costs(self) -> List["Cost"]:
        raise NotImplementedError()