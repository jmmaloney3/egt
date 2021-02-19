# -*- coding: utf-8 -*-
"""
An agent in an evolutionary game theory simulation.

Created on Sat Dec 12 23:19 2020

@author: John Maloney
"""

class Agent:
    
    '''
    Construct an agent that uses the specified strategy to choose actions.
    '''
    def __init__(self, strategy):
        self.__strategy = strategy
        self.__payout = 0
        self.__num_games = 0

    '''
    Return the action that the agent will play against the specified opponent.
    '''
    def choose_action(self, opponent):
        return self.__strategy.choose_action(opponent)

    '''
    Receive the payout for a game and increment the game count.
    '''
    def receive_payout(self, payout):
        self.__payout += payout
        self.__num_games += 1

    '''
    Reset the agent's internal state to prepare for participation in the
    next generation.
    '''
    def reset(self):
        self.__payout = 0
        self.__num_games = 0

    '''
    Return a string representation of the agent.
    '''
    def __str__(self):
        return '{0} num games: {1:3d}, payout: {2:5d}'.format(self.__strategy, \
                                                              self.__num_games, \
                                                              self.__payout)

