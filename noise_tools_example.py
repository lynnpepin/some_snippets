'''noise_tools

A collection of functions used to generate load profiles.

Load profiles  ff  are functions mapping R-->R. That is, real-value functions.

These load profiles  ff  here are from [0,1440) to values >= 0, and  are 
parameterized.

This lets a given profile  ff  be instantiated randomly with different parameters.
We also include functions to perturb ff.

1. Use  ff  as an example load-profile
2. Parameters: Contained in `Params` dataclass and generated with `generate_parameters`
3. Random instantiation: Using `ff_with_params(ff, params)`
4. Random sampling: Using `p_hv(xx, scale)` to add noise to data,
   and using `pp(ff, p_h, p_v)` to apply `p_h` and `p_v` to ff.


Example usage to generate one instance of function ff:

new_ff = pp(
    ff = ff_with_params(
        ff,
        params = generate_parameters(
            AA = np.array([8,4,2,1]),
            BB = np.array([1,2,4,8]),
            CC = np.array([0,180,120,60])
        )
    ),
    p_h = p_hv,
    p_v = p_hv
)

Example usage to generate one instance of function ff
(equivalent, but unnested):

new_AA = np.array([8,4,2,1])
new_BB = np.array([1,2,4,8])
new_CC = np.array([0,180,120,60])
new_params = generate_params(new_AA, new_BB, new_CC)
new_ff = ff_with_params(ff, new_params)
perturbed_ff = pp(new_ff, p_h = p_hv, p_v = p_hv)


Example usage to generate a series of functions from the same base ff:

base_node_functions = []
pert_node_functions = []

for ii in range(13):
    new_param = generate_parameters()
    new_ff = ff_with_params(ff, new_param)
    base_node_functions.append(new_ff)
    
    pert_ff = pp(new_ff)
    pert_node_functions.append(pert_ff)

for ii in range(13):
    plt.plot(
        range(1440),
        [pert_node_functions[ii](xx) for xx in range(1440)]
    )

Provides:

ff(xx, AA, BB, CC)

Params(self, AA, BB, CC)

generate_parameters(AA, BB, CC)

ff_with_params(ff, params)

p_hv(xx, scale)

pp(ff, p_h, p_v)


# TODO: Add unit tests?
'''

import numpy as np
import random
from dataclasses import dataclass

def ff(
    xx,
    AA = np.array([4,2,1,]),  # consider 4,2,1
    BB = np.array([1,3,5]),  # consider 1,2,4
    CC = np.array([-180, 0, -150])  # consider -180, 0, -180
):
    '''Load profile 'base' function, the sum of three sine-waves,
    adjusted so they are above the 0 line.
    
    With numpy vectors AA, BB, CC being parameters of equal length
    
    :param xx: Input value
    :type xx: float
    :param AA: Amplitude
    :type AA: np.array
    :param BB: Frequency, in (1/day). (Note that 0..1440 maps to 0..2\pi)
    :type BB: np.array
    :param CC: Offset, in minutes. 
    :type CC: np.array
    
    :returns: Sum of sine-waves according to params AA, BB, CC
    :rtype: float
    '''
    # convert xx from minutes to rads
    input_as_rads = (BB * xx + CC) * 2 * np.pi / 1440
    # (sin(...)+1)/2 to normalize from [-1,1] to [0,1]
    return sum(AA*(np.sin(input_as_rads)+1)/2)

@dataclass
class Params:
    '''Dataclass holding parameters AA, BB, CC for ff.
    
    See ff docstring for more details
    '''
    AA: np.array = np.array([4,2,1])
    BB: np.array = np.array([1,2,4])
    CC: np.array = np.array([-180, 0, -180])

    
def generate_parameters(
    AA = np.array([4,2,1]),
    BB = np.array([1,2,4]),
    CC = np.array([-180 % 1440, 0, -180 % 1440])
):
    '''
    Generate parameters used to instantiate "base" functions.
    I.e. a new instance of 'Params`.
    
    See `ff` and `Params` docstrings for more details.
    '''
    return Params(
        AA = AA + np.random.normal(scale=(AA/4), size=AA.shape),
        BB = BB,# + np.random.normal(scale=(BB/4), size=BB.shape),
        CC = CC + np.random.normal(scale=120, size=CC.shape)
    )


def ff_with_params(ff, params):
    '''Provides an instance of ff instantiated with params.
    
    Higher-order function that returns another function.
    
    :param ff:
    :type ff: function
    :param params: Instance of params, with .AA, .BB, .CC
    :type params: Params
    
    :returns: ff(xx), with parameters applied.
    :rtype: function
    '''
    def _ff(xx):
        return ff(xx, params.AA, params.BB, params.CC)
    return _ff


def p_hv(xx, scale = 1/16):
    '''A simple "perturbation function" that adds noise to values.
    
    :param xx: Value to add noise to
    :type xx: Float or numpy.array
    :param scale: The standard deviation of noise to apply 
    :type scale: Float or numpy.array with length of xx
    
    :returns: 
    :rtype: 
    '''
    return xx + np.random.normal(scale = scale)

def pp(ff, p_h = p_hv, p_v = p_hv):
    '''
    :param ff: A function on a real number
    :type ff: function
    :param p_h: The perturbation on input `xx`
    :type p_h: function
    :param p_v: The perturbation on output `ff(xx)`L
    :type p_v: function
    
    :returns: 
    :rtype: 
    '''
    def __new_ff(xx):
        return p_v(ff(p_h(xx,)))
    
    return __new_ff


# example
def _get_noise_profiles(
    ff = ff,
    nn = 15,
    AA = np.array([2/3, 1/6, 1/12, 1/24, 1/24]),
    BB = np.array([1, 2, 4, 6, 8]),
    CC = np.array([-240, 300, -180, 0, 30]),
    p_v = lambda xx: p_hv(xx, scale = 1/128),
    p_h = lambda xx: p_hv(xx, scale = 12),
):
    '''
    :param ff: The base function to start with, taking params AA, BB, CC
    :param nn: The number of functions to generate 
    :param AA, BB, CC: Parameters for ff
    :p_v: Perturb function for y value
    :p_h: Perturb function for x value
    
    Returns:
    1. basic_ff: The instance of ff with base params, no random instantiation or added noise
    2. base_ffs: List of functions with randomly-instantiated parameters
    3. pert_ffs: List of functions with randomly-instantiated parameters
                 AND noise p_v(f(p_h(x))) added on top.
    '''
    
    basic_ff = lambda xx: ff(xx, AA, BB, CC)
    
    base_ffs = []
    pert_ffs = []
    
    for ii in range(nn):
        new_param = generate_parameters(AA=AA, BB=BB, CC=CC)
        new_ff = ff_with_params(ff, new_param)
        base_ffs.append(new_ff)

        pert_ff = pp(new_ff, p_h = p_h, p_v = p_v)
        pert_ffs.append(pert_ff)
    
    return basic_ff, base_ffs, pert_ffs
