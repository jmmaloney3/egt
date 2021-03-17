# -*- coding: utf-8 -*-
"""
Utilities for input validation.

Created on Sun Mar 07 21:42 2021

@author: John Maloney
"""

import numpy as np
import math

def type_name(obj):
    '''
    Get the type name for the object

    Parameters
    ----------
    obj : object
        The object whose type name should be returned

    Returns
    -------
    type_name : str
        The name of the type of the object
    '''
    return type(obj).__name__

def check_is_array_like(x):
    '''
    Validate that the input is `array-like` and supports the following:
      - using `len(x)` to retrieve the length
      - using `x[i]` to retrieve element `i`

    Parameters
    ----------
    x : object
        Input object to check

    Raises
    ------
    ValueError
        If the object is not `array_like`
    '''
    if ( (not (hasattr(x, '__len__') or hasattr(x, '__getitem__'))) or \
         (isinstance(x, str)) ):
        msg = "'{0}' object is not array-like: {1}"
        raise ValueError(msg.format(type_name(x), x))

def check_array_dims(x, d):
    '''
    Validate that the input is `array-like` and has the specified number
    of dimensions

    Parameters
    ----------
    x : object
        Input object to check

    d : integer
        The number of dimensions `x` should have

    Raises
    ------
    ValueError
        If the object is not `array_like` or does not have the specified number
        of dimensions
    '''
    # verify that x is array-like
    check_is_array_like(x)

    # verify that x has the correct number of dimensions
    try:
        dims = len(x.shape)
        if (dims != d):
            msg = "'{0}' has {1} dimensions, expected {2}: {3}"
            raise ValueError(msg.format(type_name(x), dims, d, x))
    except AttributeError:
        if (d != 1):
            msg = "'{0}' has {1} dimensions, expected {2}: {3}"
            raise ValueError(msg.format(type_name(x), 1, d, x))

def check_is_prob_dist(x):
    '''
    Validate that the input is a valid probability distriution:
      - 1-dimensional `array-like`
      - elements are numeric values between `0` and `1`
      - elements sum to `1`

    Parameters
    ----------
    x : object
        Input object to check

    Raises
    ------
    ValueError
        If the object is not a probability distribution
    '''
    # check that x is a 1-dimensional array
    check_array_dims(x, 1)

    # check that elements of x are valid probabilities
    try:
        # supported by numpy arrays
        if (any(x<0) or any(x>1)):
            msg = "one or more values in '{0}' are not valid probabilities: {1}"
            raise ValueError(msg.format(type_name(x), x))
    except TypeError:
        # support for tuples and lists
        if (any(i<0 for i in x) or (any(i>1 for i in x))):
            msg = "one or more values in '{0}' are not valid probabilities: {1}"
            raise ValueError(msg.format(type_name(x), x))

    if (not math.isclose(np.sum(x), 1)):
        msg = "'{0}' values do not sum to 1: {1}"
        raise ValueError(msg.format(type_name(x), x))

def check_is_combined_pure_payoff_function(p):
    '''
    Validate that the object is a valid combined pure strategy payoff function.

    Parameters
    ----------
    x : object
        Input object to check

    Raises
    ------
    ValueError
        If the object is not a valid combined pure strategy payoff function

    Notes
    -----
    Only 2-player games are currently supported.
    '''
    # check that p is a 1-D array
    check_array_dims(p, 1)

    # check that p has two payoff functions - one for each player
    if (len(p) != 2):
        msg = "'{0}' has payoff functions for {1} players but only 2 are supported"
        raise ValueError(msg.format(type_name(p), len(p)))

    # make sure each element of p is a 2-D array
    check_array_dims(p[0], 2)
    check_array_dims(p[1], 2)

    # make sure the matrices are compatible
    if ( (p[0].shape[0] != p[1].shape[1]) or (p[0].shape[1] != p[1].shape[0]) ):
        msg = "{0}x{1} matrix is not compatible with {2}x{3} matrix"
        raise ValueError(msg.format(p[0].shape[0], p[0].shape[1], \
                                    p[1].shape[0], p[1].shape[1]))
