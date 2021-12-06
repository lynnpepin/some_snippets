'''einsum_examples.py

'Einsum' is a one-function-to-rule-them-all that generalizes a whole
lot of matrix / tensor operations.

For example, matrix multiplication between A and B in pytorch:
    torch.einsum('ik,kj->ij', [A, B])

It's implemented in Numpy, PyTorch, Tensorflow, and others, and uses a string
language (a-la regex), so it's hypothetically portable.

Examples are taken from here: https://rockt.github.io/2018/04/30/einsum

Einstein Sum notation can be further generalized. Check this out: https://github.com/arogozhnikov/einops
'''

import numpy as np
import torch
import tensorflow as tf

def get_tensors_from_numpy(A):
    # From numpy array A, return a Torch tensor and a Tensorflow tensor
    return torch.from_numpy(A), tf.convert_to_tensor(A)


# 1. Matrix transpose
A = np.array(
    [[0, 1, 2],
     [3, 4, 5]]
)
A_pyt, A_tf = get_tensors_from_numpy(A)

np.einsum('ij->ji', A)
torch.einsum('ij->ji', A_pyt)
tf.einsum('ij->ji', A_tf)


# 2. 

# wait these will all just be exactly the same huh
