#!/usr/bin/env python3
from .Cost import Cost
import pandas as pd
from .Interval import Interval

class ConstIncreaseWrapper(Cost):
    """
    Wraps a cost model and modifies it so that 
    """
    def __init__(self, name, cost_function):