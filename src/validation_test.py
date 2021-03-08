# -*- coding: utf-8 -*-
"""
Tests for validation.py

Created on Sun Mar 07 22:43 2021

@author: John Maloney
"""

import numpy as np
import pytest

import validation

'''
Test array-like validation logic
'''
def test_check_is_array_like():
    # array-like objects
    test_objects = (
        np.array([1,2]), # 1-dim array is array-like
        np.array([[1,2],[3,4]]), # 2-dim array is array-like
        np.array([]), # empty array is array-like
        [1,2], # list is array-like
        [[1,2],[3,4]], # list of lists is array-like
        [], # empty list is array-like
        (1,2), # tuple is array-like
        (), # empty tuple is array-like
        (True, "hello"), # contents do not matter
        ([1,2], np.array([3,4]))
    )
    for test_obj in test_objects:
        validation.check_is_array_like(test_obj)

    # NOT array-like objects
    test_objects = (
        1, # single number is not array-like
        "string", # string is not array-like
        True # boolean is not array-like
    )
    for test_obj in test_objects:
        with pytest.raises(ValueError):
            validation.check_is_array_like(test_obj)

'''
Test dimension checking logic
'''
def test_check_array_dims():
    # checking array dims first checks that object is array-like
    with pytest.raises(ValueError):
        # number 1 is not an array-like object
        validation.check_array_dims(1, 3)

    # 1-D array-like objects
    test_objects = (
        np.array([1,2]),
        [1,2,3,4],
        (1,2,3,4,5,6),
        [],
        (),
        np.array([])
    )
    for test_obj in test_objects:
        validation.check_array_dims(test_obj, 1)
    
    # 2-D array-like object
    validation.check_array_dims(np.array([[1,1],[2,2]]), 2)
    validation.check_array_dims(np.array([[[1,1],[2,2]]]), 3)

    # error conditons
    with pytest.raises(ValueError):
        validation.check_array_dims([1,2], 2)
        validation.check_array_dims([[1,2],[2,2]], 2)
        validation.check_array_dims(np.array([[1,2],[2,3]]), 1)
        validation.check_array_dims((1), 2)