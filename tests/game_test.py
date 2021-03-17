"""
Tests for game.py

Created on Sat Mar 06 23:09 2021

@author: John Maloney
"""
import numpy as np
import pytest

import game

'''
Test calculating the expected payoffs for a 2-person normal
form game.
'''
def test_expected_payoffs():
    # payoff matrices
    p0 = np.array([[1,2,3], [4,5,6]])
    p1 = np.array([[6,5], [4,3], [2,1]])
    p = [p0, p1]

    # mixed strategies
    x0 = [0.25, 0.75]
    x1 = [0.25, 0.5, 0.25]
    x = [x0, x1]

    u = game.expected_payoffs(x,p)

    assert u[0] == 4.25
    assert u[1] == 3.25

def test_expected_payoff_errors():
    # payoff matrices
    p0 = np.array([[1,2,3], [4,5,6]])
    p1 = np.array([[6,5], [4,3], [2,1]])

    # mixed strategies
    x0 = [0.25, 0.75]
    x1 = [0.25, 0.5, 0.25]

    with pytest.raises(ValueError):
        p = [p0, p1]
        x = [x1, x0]
        game.expected_payoffs(x,p)

    with pytest.raises(ValueError):
        p = [p1, p0]
        x = [x0, x1]
        game.expected_payoffs(x,p)