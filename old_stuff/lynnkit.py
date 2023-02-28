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

def equi_hash(n, a = 0.618033988749895, K = 131072):
    """Hash integer n to range [0, K) using Equidistribution Theorem Hash, using irrational a.

    Is optimal for a = Phi = 1.618034.
    Because of mod 1, we use 0.618034.

    :param n: Input to hash
    :type n: int
    :param a: Irrational number, defaults to 0.618033988749895
    :type a: float, optional
    :param K: [description], defaults to 131072
    :type K: int, optional

    :return: Result of the hash: An int in range [0, K)
    :rtype: int
    """
    return math.floor(((n * a) % 1)*K)



def flatten(x):
    """Recursively flatten x, where x can be:
     * A dict where leaf values are array-like or other iterable:
     * An array-like, or
     * An int/float.

    Useful for converting a model.grid_state dict to a raw numpy array.

    Example usage:
    flatten(model.grid_state)

    # Warning - can take about 1GB of RAM for 1440 timesteps.
    # will have 1441 elements.
    timeline = np.stack([flatten(grid_state) for grid_state in model.grid_timeline])
    """
    if type(x) is np.ndarray:
        return x
    elif type(x) is dict:
        return np.concatenate(np.array([flatten(x[k]) for k in x.keys()]))
    elif type(x) in (list, tuple):
        return np.concatenate(np.array([flatten(v) for v in x]))
    elif type(x) is set:
        return np.concatenate(np.array([flatten(v) for v in list(x)]))
    elif type(x) in (float, int):
        return np.array([float(x)])
    elif type(x) is str:
        return np.array([float(x)])



# return a flat list of float, int, str
# or none if the object has no indices

def flatten_indices(x, sep = ' ', depth=0, max_depth=-1):
    """Recursively flatten the indices of an iterable to a list of strings.

    >>> flatten({'a' : 1, 'b' : [1, 2, [10, 20]], 'c'  : {'x' : 100, 'y' : 200}})
    [1, 1, 2, 10, 20, 100, 200]
    >>> flatten_indices(flatten({'a' : 1, 'b' : [1, 2, [10, 20]], 'c'  : {'x' : 100, 'y' : 200}}))
    ['a', 'b 0', 'b 1', 'b 2 0', 'b 2 1', 'c x', 'c y']


    :param x: An iterable or value.
    :type x: dict | float | int | str | None
    :param sep: Separator for string representation of keys, defaults to ' '
    :type sep: str, optional
    :param depth: Current depth, defaults to 0
    :type depth: int, optional
    :param max_depth: Maximum depth to record. Defaults to unbounded, defaults to -1
    :type max_depth: int, optional
    :return: List representing the indices used in X, recursive.
    :rtype: list of str
    """
    
    if depth == max_depth:
        # Do not return anything deeper than this depth
        return None
    
    if type(x) in (float, int, str):
        return None
    elif type(x) is dict:
        indices = x.keys()
    elif type(x) in (list, tuple):
        indices = range(len(x))
    
    flattened_indices = []
    
    for idx in indices:
        child = x[idx]
        child_indices = flatten_indices(child, depth+1)
        
        if child_indices is None:
            # child is float, int, or str
            # so just add ur index to the flattened indices
            flattened_indices.append(str(idx))
        else:
            # child is iterable
            for child_idx in child_indices:
                flattened_indices.append(str(idx) + sep + child_idx)
    
    return flattened_indices
