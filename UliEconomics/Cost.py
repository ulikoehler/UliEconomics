#!/usr/bin/env python3
from abc import ABC, abstractmethod
import pandas as pd

class Cost(ABC):
    
    @abstractmethod
    def in_period(self, start: pd.Timestamp, end: pd.Timestamp) -> float:
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
    def shift(self, num: float, unit: str) -> None:
        """
        Shift this cost by a given timedelta.
        Positive timedeltas shift to the future.
        Negative timedeltas shift to the past.
        
        For some types of timedeltas, this has no effect.
        """
        raise NotImplementedError()