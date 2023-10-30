#!/usr/bin/python3
"""Module to multiplies 2 matrices by using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices

    Args:
        m_a (list): list 1 of lists of integers or floats
        m_b (list): list 2 of lists of integers or floats

    Returns:
        a new matrix which is the product of the argument
        i.e ```m_a • m_b```; otherwise return error
    """

    return np.matmul(m_a, m_b)
