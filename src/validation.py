# -*- coding: utf-8 -*-
"""
Utilities for input validation.

Created on Sun Mar 07 21:42 2021

@author: John Maloney
"""

import numpy as np

'''
Get the type nme for the object

Parameters
----------
obj : object
  The object whose type name shoudl be returned
'''
def type_name(obj):
    return type(obj).__name__

'''
Validate that the input is array-like and supports the following:
  - using len(x) to retrieve the length
  - using x[i] to retrieve element i

Parameters
----------
x : object
  Input object to check
'''
def check_is_array_like(x):
    if ( (not (hasattr(x, '__len__') or hasattr(x, '__getitem__'))) \
         or (isinstance(x, str)) ):
        msg = "{0} object is not array-like"
        raise ValueError(msg.format(type_name(x)))

'''
Validate that the input is array-like and has the specified number of dimensions

Parameters
----------
x : object
  Input object to check

d : integer
  The number of dimensions x should have
'''
def check_array_dims(x, d):
    # verify that x is array-like
    check_is_array_like(x)

    # verify that x has the correct number of dimensions
    try:
        dims = len(x.shape)
        if (dims != d):
            msg = "{0} has {1} dimensions, expected {2}"
            raise ValueError(msg.format(type_name(x), dims, d))
    except AttributeError:
        if (d != 1):
            msg = "{0} has {1} dimensions, expected {2}"
            raise ValueError(msg.format(type_name(x), 1, d))

'''
Validate that the input is a valid probability distriution:
  - 1-dimensional array-like
  - elements are numeric values between 0 and 1
  - elements sum to 1
'''
def check_is_prob_dist(x):
    # check that x is an array-like object
    check_is_array_like(x)

    # check that x is a 1-dimensional array
    check_array_dims(x, 1)

    # check that elements of x are valid probabilities
    if (any(x<0) or any(x>1)):
        msg = "one or more values in {0} are not valid probabilities"
        raise ValueError(msg.format(type_name(x)))

    if (np.sum(x) != 1):
        msg = "{0} values do not sum to 1"
        raise ValueError(msg.format(type_name(x)))








    