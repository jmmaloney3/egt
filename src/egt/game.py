# -*- coding: utf-8 -*-
"""
A set of capabilities for defining the stage games that are used in
evolutionary game theory (EGT) simulations.  This module currently only
suports symmetric two-player normal form games.  These are games where
the following holds:

* There are exactly two player positions
* Each player position has the same numer of pure strategies (k)
* Payoff function is independent of player position

Given these constraints, the game and the strategies used by agents playing
the game can be represented as follows:

* The payoff function is represented as a k x k matrix where k is the number
  of pure strategies in the game
* A mixed strategy is represented as a k-vector where each component of the 
  vector represents the probability that the agent plays the corresponding
  pure strategy.  A pure strategy is represented as a k-vectors with one
  component equal to one and the remaining components equal to zero.

Created on Thu Dec 17 21:40 2020

@author: John Maloney
"""
import numpy as np

'''
Calculate the expected payoffs for the two mixed strategies playing a
one-shot symmetric two player normal form game.

Parameters
----------

x : vector
  k-vector defining the mixed strategy for the first player

y : vector
  k-vector defining the mixed strategy for the second player

A : array-like
  k x k matrix defining the payoffs for a two-player symmetric normal
  form game

Returns
-------
u : vector
    2-vector whose components are the expected payoffs for the two
    mixed strategies
'''
def expected_payoffs(x, y, A):
    ux = np.dot(np.dot(x, A), y)
    uy = np.dot(np.dot(y, A), x)
    return np.array([ux, uy])

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