'''lynnkit.py

A collection of various, unrelated functions that I use often.

This is made by me for me, but you can use it too!
'''

# todo:

# simple socket client, server

# normal map code

def fib(nn: int) -> int:
    '''Returns the nth value in the fibonacci sequence

    :param nn: The index of the value to generate for the fibonacci sequence
    :type nn: int
    
    :raises ValueError: for values < 0
    :raises TypeError:  for non-int input

    :returns: The (nn)th value of the fibonacci sequence
    :rtype: int

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(10)
    55
    >>> fib(-1)
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci sequence can not be evaluated on negative index
    >>> fib(3.1)
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci sequence can only be indexed over integers
    
    '''
    if not type(nn) is int:
        raise TypeError("Fibonacci sequence can only be indexed over integers")
    if nn < 0:
        raise TypeError("Fibonacci sequence can not be evaluated on negative index")
    vals = [0, 1]
    for ii in range(0, nn):
        vals[ii%2] += vals[(ii+1)%2]
    
    return vals[nn%2]


def fibgen():
    """Provides a generator yielding the  fibonacci sequence
    
    :yields: int
    :returns: An iterator which yields the i-th value of the Fibonacci sequence
        for each i-th call of next() on an instance of fibgen
    :rtype: Iterator[int]

    >>> f = fibgen()
    >>> next(f)
    0
    >>> next(f)
    1
    >>> next(f)
    1
    >>> next(f)
    2
    >>> next(f)
    3
    """
    
    vals = [0, 1]
    ii = 0
    while True:
        yield vals[ii%2]
        vals[ii%2] += vals[(ii+1)%2]
        ii += 1
