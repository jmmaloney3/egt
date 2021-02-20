# -*- coding: utf-8 -*-
"""
An agent population for an evolutionary game theory simulation.
The population tracks the agents in the population and determines
the relationships between those agents.

Created on Tue Feb 16 22:07 2021

@author: John Maloney
"""

class Population:

    '''
    Construct an agent population with the specified initial population
    and relationships.
    '''
    def __init__(self, agents):
        self.__agents = agents

    '''
    Return a generator that provides the agent matches for a populaton.  These
    are the pairs of agents that should play a game during a single round of
    the simulation.

    The matches returned by this generator generally depends on the structure
    of the population.  For example, if the population is embedded in a grid
    then, in general, this will return pairs of agents that are neighbors on
    the grid.
    '''
    def matches(self):
        for i in range(len(self.__agents)):
            for j in range(i+1, len(self.__agents)):
                yield (self.__agents[i], self.__agents[j])
