'''function_perturbator.py

WIP

A collection of functions and methods used to:

1. Linearly interpolate and wrap-index lists and list-likes

2. Use stochastic elements to sample from some real function f(x)
'''

import random
import numpy as np



class linlist(list):
    # TODO docstring, etc.
    def __getitem__(self, x):
        # TODO
        return super().__getitem__(x)
    
    def __setitem__(self, key, value):
        # TODO
        super().__setitem__(key, value)
    
    def index(self, value, start=0, stop=9223372036854775807):
        # TODO
        return super().index(value)

# Examples
def get_base_function():
    # TODO
    # f(x) should be a sum of a series of sin-waves
    # i.e. sum([ a * sin(t*b + c) for a,b,c in ...])
    # where a is amplitude, b is frequency, c is phase-shift
    pass

def get_perturbation():
    pass
