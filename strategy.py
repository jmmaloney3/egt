# -*- coding: utf-8 -*-
"""
A strategy for playing a 2-player game.

Created on Sat Dec 19 22:41 2020

@author: John Maloney
"""

class Strategy:
    '''
    Choose an action to play given the specified opponent.
    '''
    def choose_action(self, opponent):
        return 0

class Pure0:
    '''
    A straegy that always selects action 0 regardless of the opponent.
    '''
    def choose_action(self, opponent):
        return 0

class Pure1:
    '''
    A straegy that always selects action 1 regardless of the opponent.
    '''
    def choose_action(self, opponent):
        return 1
