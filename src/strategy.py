# -*- coding: utf-8 -*-
"""
A strategy for playing a 2-player game.

Created on Sat Dec 19 22:41 2020

@author: John Maloney
"""

class Strategy:
    '''
    Create a generic strategy.
    '''
    def __init__(self):
        self._name = "Generic Strategy"

    '''
    Choose an action to play given the specified opponent.
    '''
    def choose_action(self, opponent):
        return 0

    '''
    Return a string representation of the strategy.
    '''
    def __str__(self):
        return '<strategy: {0}>'.format(self._name)

class Pure(Strategy):
    '''
    Create a pure strategy that always chooses the specified action.
    '''
    def __init__(self, action):
        self.__action = action
        self._name = "Pure" + str(action)


    '''
    Return the action specified by this pure stategy.
    '''
    def choose_action(self, opponent):
        return self.__action
