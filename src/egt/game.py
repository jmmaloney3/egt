# -*- coding: utf-8 -*-
"""
A two person game.

Created on Thu Dec 17 21:40 2020

@author: John Maloney
"""
import numpy as np

'''
Calculate the expected payoffs for a players in a 2-player normal form game
where:
  - n   : number of players, in this case n = 2
  - m_i : number of pure strategies available to player i
  - x_i : vector of length m_i representing the mixed strategy for player i
  - p_i : m_i x m_j dimension matrix specifying the pure strategy payoff
          function for player i

Parameters
----------
x : array-like
    The mixed strategy profile being played where x[i] is the mixed strategy
    for player i

p : array-like
    The combined pure strategy payoff function where p[i] is a m_i x m_j matrix
    specifying the pure strategy payoff function for player i

Returns
-------
u_x : array-like
    The expected payoffs where u_x[i] is the expected payoff for player i
'''
def expected_payoffs(x, p):
    _check_arrays(x, p)

    u0 = np.dot(x[0], np.dot(p[0],x[1])) # expected payoff for player 0
    u1 = np.dot(x[1], np.dot(p[1],x[0])) # expected payoff for player 1

    return np.array([u0, u1])

def _check_arrays(x, p):
    m_0 = len(x[0])
    m_1 = len(x[1])

    err_msg = "{0} incompatible with mixed strategy vectors"
    if (p[0].shape != (m_0, m_1)):
        raise ValueError(err_msg.format("p[0]"))

    if (p[1].shape != (m_1, m_0)):
        raise ValueError(err_msg.format("p[1]"))

class Game:

    '''
    Create a 2-player normal-form game with the specified strategy names and payouts.

    Parameters
    ----------
    payouts : 3D array specifying the payouts for each player structured such that the
              indices are the following: [row, column, player]
    '''
    def __init__(self, payoff_matrix):
        self.payoff_matrix = payoff_matrix

    '''
    Get the payouts for the specified strategy choices.

    Parameters
    ----------
    key : strategy selections for the two players: player1, player2
    '''
    def __getitem__(self, key):
        return self.payoff_matrix[key]

    '''
    Return a string representation of the game.
    '''
    def __str__(self):
        str = "---------------\n"
        for i in (0,1):
            str += '{0:2d}, {1:2d} | {2:2d}, {3:2d}'.format(self.payoff_matrix[i,0,0], \
                                                            self.payoff_matrix[i,0,1], \
                                                            self.payoff_matrix[i,1,0], \
                                                            self.payoff_matrix[i,1,1])
            str += "\n"
        str += "---------------\n"
        return str