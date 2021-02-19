# -*- coding: utf-8 -*-
"""
An two person game.

Created on Thu Dec 17 21:40 2020

@author: John Maloney
"""

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