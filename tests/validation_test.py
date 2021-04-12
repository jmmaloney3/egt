# -*- coding: utf-8 -*-
"""
Tests for validation.py

Created on Sun Mar 07 22:43 2021

@author: John Maloney
"""

import numpy as np
import pytest

from egt import validation

def test_check_is_array_like():
    '''
    Test array-like validation logic
    '''
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

def test_check_array_dims():
    '''
    Test dimension checking logic
    '''
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

def test_check_is_prob_dist():
    '''
    Test probability distribution checking logic
    '''
    # checking prob dist first checks that object is array-like
    with pytest.raises(ValueError):
        # number 1 is not an array-like object
        validation.check_is_prob_dist(1)

    # checking prob dist next checks that object is 1-dim array
    with pytest.raises(ValueError):
        # 2-D array raises exception
        validation.check_is_prob_dist(np.array([[1,2],[2,3]]))

    # probability distributions
    test_objects = (
        np.array([1]),
        np.array([0.25,0.75]),
        np.array([1,0]),
        [1], [0.4, 0.6], [0,1],
        (0.85, 0.15), (1,0,0),
        np.array([1/3,1/3,1/6,1/6]),
        np.array([0.2499999999,0.7499999999])
    )
    for test_obj in test_objects:
        validation.check_is_prob_dist(test_obj)

    # NOT probability distributions
    test_objects = (
        np.array([0.99999999]),
        np.array([0.250000001,0.75]),
        np.array([1,0.000000001]),
        [1.000000001], [0.5, 0.499999999], [0.000000001,1],
        (0.850000009, 0.15), (1,0,0.000000001),
        np.array([1/3,1/3,1/6,1/5]),
        np.array([0.24999999,0.74999999])
    )
    for test_obj in test_objects:
        with pytest.raises(ValueError):
            validation.check_is_prob_dist(test_obj)

def test_is_combined_pure_payoff_function():
    '''
    Test combined pure strategy payoff function validation logic.
    '''
    matrix1 = np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])
    matrix2 = np.array([[1,2,3],[4,5,6],[7,8,9],[0,1,2]])
    test_obj = (matrix1, matrix2)

    validation.check_is_combined_pure_payoff_function(test_obj)

    test_obj = (matrix1, matrix2.T)
    with pytest.raises(ValueError):
        validation.check_is_combined_pure_payoff_function(test_obj)