# -*- coding: utf-8 -*-
"""
An example evolutionary game theory simulation.

Created on Sat Dec 18 23:04 2020

@author: John Maloney
"""

import numpy as np
import agent
import game
import strategy
import simengine

def main():
    # create the prisoner's dilemma game
    T = 5 # temptation to defect
    R = 3 # reward for mutual cooperation
    P = 1 # punishment for mutual defection
    S = 0 # sucker's payoff
    PD_matrix = np.array([[[R,R], [S,T]], \
                          [[T,S], [P,P]]])
    PD = game.Game(PD_matrix)

    # create the cooperating agents
    cstrat = strategy.Pure0()
    cagents = [agent.Agent(cstrat) for j in range(15)]

    # create the defecting agents
    dstrat = strategy.Pure1()
    dagents = [agent.Agent(dstrat) for j in range(5)]

    # create the simulation engine & play matches
    sim = simengine.SimEngine(PD, np.concatenate((cagents,dagents)))
    print(sim.play_matches())


    print(PD)

    for a in np.concatenate((cagents,dagents)):
        print(a)

# run main method when this file is run from command line
if __name__ == "__main__":
    main()