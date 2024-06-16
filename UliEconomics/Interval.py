#!/usr/bin/env python3
import pandas as pd

class Interval(object):
    """
    Represents an interval [start, end)
    Note that [end] is not included in the interval
    """
    def __init__(self, start: pd.Timestamp, end: pd.Timestamp):
        self.start = start
        self.end = end
        assert self.start <= self.end
        
    def size(self) -> pd.Timedelta:
        return self.end - self.start
        
    def includes(self, timestamp: pd.Timestamp) -> bool:
        return timestamp >= self.start and timestamp < self.end
    
    def shift(self, timedelta: pd.Timedelta) -> "Interval":
        return Interval(
            self.start + timedelta,
            self.end + timedelta
        )

    def has_overlap(self, other: "Interval"):
        # If end is identical => no overlap, because interval doesn't include end
        return other.includes(self.start) or (
            other.includes(self.end) and self.end != other.end
        )
    
    def __mul__(self, factor: float) -> "Interval":
        """
        Shrink or grow the interval by a given factor.
        Note that the start point is kept the same,
        only the end point will change.
        
        Factors > 1.0 will grow the interval
        Factors < 1.0 will shrink the interface
        """
        return Interval(
            self.start,
            self.start + self.size() * factor 
        )
    
    def __str__(self) -> str:
        return f"{self.start} .. {self.end}"
    
    def __repr__(self) -> str:
        return f"Interval({self.__str__()})"