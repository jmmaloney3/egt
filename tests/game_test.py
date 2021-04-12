"""
Tests for game.py

Created on Sat Mar 06 23:09 2021

@author: John Maloney
"""
import numpy as np
import pytest

from egt import game

'''
Test calculating the expected payoffs for a one-shot 2-person
symmetric normal form game when pure strategies are used.
'''
def test_expected_payoffs_pure():
    # payoff matrix: prisoner's dilemma
    PD = np.array([[4, 0],
                   [5, 3]])

    # pure strategies; cooperate & defect
    C = [1, 0]
    D = [0, 1]

    u = game.expected_payoffs(C, D, PD)
    assert u[0] == 0
    assert u[1] == 5

    # save values for next test case
    v = u

    u = game.expected_payoffs(D, C, PD)
    assert u[0] == v[1] # because the game is symmetric
    assert u[1] == v[0] # because the game is symmetric

    u = game.expected_payoffs(C, C, PD)
    assert u[0] == 4
    assert u[1] == u[0] # because the game is symmetric

    u = game.expected_payoffs(D, D, PD)
    assert u[0] == 3
    assert u[1] == u[0] #because the game is symmetric

'''
Test calculating the expected payoffs for a one-shot 2-person
symmetric normal form game when mixed strategies are used.
'''
def test_expected_payoffs_mixed():
    # payoff matrix: prisoner's dilemma
    PD = np.array([[4, 0],
                   [5, 3]])

    # mixed strategies
    C = [0.75, 0.25]
    D = [0.25, 0.75]

    u = game.expected_payoffs(C, D, PD)
    assert u[0] == 1.625
    assert u[1] == 4.125

    # save values for next test case
    v = u

    u = game.expected_payoffs(D, C, PD)
    assert u[0] == v[1] # because the game is symmetric
    assert u[1] == v[0] # because the game is symmetric

    u = game.expected_payoffs(C, C, PD)
    assert u[0] == 3.375
    assert u[1] == u[0] # because the game is symmetric

    u = game.expected_payoffs(D, D, PD)
    assert u[0] == 2.875
    assert u[1] == u[0] # because the game is symmetric

'''
Test calculating the expected payoffs for a one-shot 2-person
symmetric normal form game when mixed strategies are used.

Test using a game with more than two pure strategies.
'''
'''
def test_expected_payoffs_mixed2():
    # payoff matrix: modified prisoner's dilemma
    PD = np.array([[4, 0, 0],
                   [2, 2, 2],
                   [5, 0, 3]])

    # mixed strategies
    C = [0.5, 0.3, 0.2]
    D = [0.2, 0.3, 0.5]

    u = game.expected_payoffs(C, D, PD)
    assert u[0] == 0.96
    assert u[1] == 1.549999999999998

    # save values for next test case
    v = u

    u = game.expected_payoffs(D, C, PD)
    assert u[0] == v[1]
    assert u[1] == v[0]

    u = game.expected_payoffs(C, C, PD)
    assert u[0] == 2.22
    assert u[1] == u[0]

    u = game.expected_payoffs(D, D, PD)
    assert u[0] == 0.5475
    assert u[1] == u[0]
'''

'''
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
'''