# -*- coding: utf-8 -*-
"""
An engine for evolutionary game theory simulations.

Created on Sat Dec 12 23:33 2020

@author: John Maloney
"""

import agent
import population
import strategy

class SimEngine:

    '''
    Create an engine to run an evolutionary game theory simulation. 
    '''
    def __init__(self, game, agents):
        self.__game = game
        self.__population = population.Population(agents)
        self.__total_payouts = 0

    '''
    Run the simulation for the specified number of generations.
    '''
    def run(self, gens=100):
        for g in range(gens):
            s = 'start generation: {0:5d}'.format(g)
            print(s)

            # play matches for this generation
            self.play_matches()

            # evolve population
            # -- TBD

            # reset engine for next generation
            self.reset()

            s = '  end generation: {0:5d}'.format(g)
            print(s)

    '''
    Play the matches for one time period.
    '''
    def play_matches(self):
        for pair in self.__population.matches():
            self.__total_payouts += self.play_match(pair[0], pair[1])

            s = '({0}, {1}): | {2:3d}'.format(pair[0], pair[1], self.__total_payouts)
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
        self.__population.reset()