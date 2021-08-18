# Example of using function decorators in Python

import sys
import time
import random
import numpy as np

# We use syntactic sugar available in newer versions of Python
print(sys.version)

# Example 1: An identity decorator
# this wraps, but does not otherwise modify, a function
def identity_decorator(func):
    def wrapped_function(*args, **kwargs):
        # code goes here
        result = func(*args, **kwargs)
        # code goes here
        
        # then, return the result from the decorated function
        return result
    
    return wrapped_function

# this is equivalent to identity_decorator(lambda x: x**2)
@identity_decorator
def f(x):
    return x**2

# Example 2: A timing wrapper
def timerwrapper(func):
    def timedfunc(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        duration = end_time - start_time
        return result, duration
    
    return timedfunc

# Example 3: A "user prompt" wrapper
def prompt_before_run(func):
    def prompted(*args, **kwargs):
        while True:
            user_input = input(f"Do you want to run {func.__name__}? (yes/no/args/help)")

            if user_input.lower() == 'yes':
                return func(*args, **kwargs)
            elif user_input.lower() == 'no':
                return None
            elif user_input.lower() == 'args':
                print("Printing arguments for this function...")
                print(args)
                print(kwargs)
                print("... done!")
            elif user_input.lower() == 'help':
                print("Type a command and press Enter:")
                print("  'yes'  : Run this function")
                print("  'no'   : Do not run this function")
                print("  'args' : Print the arguments and then ask again before running")
                print("  'help' : Display this menu")
    
    return prompted

# Using examples 2 and 3 on a 'random walk' function.
@prompt_before_run
def random_walk(n):
    # a random walk with n steps
    s = 0
    for __ in range(n):
        s += (random.random() -.5)*2
    
    return s

walk_val = random_walk(1000)
walk_val = random_walk(1000000)

# You can even use two!

@timerwrapper
@prompt_before_run

def random_walk(n):
    # a random walk with n steps
    s = 0
    for __ in range(n):
        s += (random.random() -.5)*2
    
    return s

walk_val, runtime = random_walk(10000)
print(f"Got value {walk_val:.2f} in time {runtime:.2f}")
