#!/usr/bin/python3

"""
Defines a function lazy_matrix_mul using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the multiplication of two matrices.

    Args:
        m_a: first matrix.
        m_b: second matrix.
    """

    return (np.matmul(m_a, m_b))
