#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd
from .Interval import Interval
from typing import List

class CombinedCost(Cost):
    """
    Represents a cost combined from an arbitrary list of
    individual sub-costs.
    All behavious is delegated to the individual costs.
    """
    def __init__(self, name, costs: List[Cost]):
        self.name = name
        self.costs = costs
    
    def is_continous(self) -> bool:
        return True
    
    def copy(self) -> "CombinedCost":
        return CombinedCost(self.name,
                            costs=self.costs)

    def shift(self, timedelta: pd.Timedelta) -> "CombinedCost":
        # Just shifts every individual cost position
        return CombinedCost(
            name=self.name,
            costs=[
                cost.shift(timedelta)
                for cost in self.costs
            ]
        )
    
    def cost_in_interval(self, interval: Interval) -> float:
        return sum(
            cost.cost_in_interval(interval)
            for cost in self.costs
        )
    
    def __mul__(self, other: float) -> "CombinedCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.#
        """
        # Just multiplies every individual cost position
        return CombinedCost(
            name=self.name,
            costs=[
                cost * other
                for cost in self.costs
            ]
        )
        
    def __imul__(self, other: float) -> "CombinedCost":
        """
        Multiply this cost by a scalar. This just increases the cost by a given factor.
        This is the inplace version of __mul__.
        """
        self.costs = [
            cost * other
            for cost in self.costs
        ]
        return self
    
    def __str__(self) -> str:
        return ", ".join(cost.__str__() for cost in self.costs)
    
    def __repr__(self) -> str:
        return f"CombinedCost({self.name}: {', '.join(cost.__repr__() for cost in self.costs)}))"
    
    def sub_costs(self) -> List[Cost]:
        return []