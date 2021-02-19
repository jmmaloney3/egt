# -*- coding: utf-8 -*-
"""
An engine for evolutionary game theory simulations.

Created on Sat Dec 12 23:33 2020

@author: John Maloney
"""

import agent
import strategy

class SimEngine:

    '''
    Create an engine to run an evolutionary game theory simulation. 
    '''
    def __init__(self, game, agents):
        self.__game = game
        self.__agents = agents
        self.__total_payouts = 0

    '''
    Play the matches for one time period.
    '''
    def play_matches(self):
        # need a configurable way to select agents for the matches
        # TEMP: each agent plays against every other agent exactly once
        for i in range(len(self.__agents)):
            for j in range(i+1, len(self.__agents)):
                self.__total_payouts += self.play_match(self.__agents[i], self.__agents[j])

                s = '({0:3d}, {1:3d}): | {2:3d}'.format(i, j, self.__total_payouts)
                print(s)

        # return the total payouts for use by the sim engine
        return self.__total_payouts

    '''
    Play a single match between two agents:
     - Select actions for each agent
     - Calculate payouts
     - Update payouts for agents and the simulation
    '''
    def play_match(self, row_player, col_player):
        # select action
        row_strat = row_player.choose_action(col_player)
        col_strat = col_player.choose_action(row_player)
        # calcuate payouts
        row_po, col_po = self.__game[row_strat, col_strat]
        # pay payouts
        row_player.receive_payout(row_po)
        col_player.receive_payout(col_po)

        return row_po + col_po

    '''
    Reset the engine to prepare to simulate the next generation.
    '''
    def reset(self):
        self.__total_payouts = 0
        for a in self.__agents:
            a.reset()