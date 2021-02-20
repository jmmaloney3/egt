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
        self.name = "Generic Strategy"

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

class Pure0(Strategy):
    '''
    Create a Pure0 strategy.
    '''
    def __init__(self):
        self._name = "Pure0"

    '''
    A straegy that always selects action 0 regardless of the opponent.
    '''
    def choose_action(self, opponent):
        return 0

class Pure1(Strategy):
    '''
    Create a Pure0 strategy.
    '''
    def __init__(self):
        self._name = "Pure1"

    '''
    A straegy that always selects action 1 regardless of the opponent.
    '''
    def choose_action(self, opponent):
        return 1
