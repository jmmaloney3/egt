# -*- coding: utf-8 -*-
"""
A module that provides implementations for common versions of
evolutionary dynamics.

Created on Tue Mar 06 12:07 2021

@author: John Maloney
"""

import numpy as np

'''
Evolve the population using the discrete replicator dynamics.

Parameters
----------
x : array-like
    A population state where x[i] is a value between 0 and 1 specifying the
    proportion of the population using strategy i in the current time step.

f : array-like
    A vector of fitness values where f[i] is the fitness of type i in
    population state x

Returns
-------
x2 : array-like
    A new population state where x[i] specifies the proportion of the
    population using strategy i in the next time step.
'''
def rep_dynamics(x, f):
    # calculate the average population fitness in state x
    avg_f = np.dot(x, f)

    return x*(f / avg_f)

'''
An impementation of the discrete replicator dynamcs for a simultaneous
symmetric 2-player normal form game.  The game is assumed to have the
following characteristics:
  - There are N pure strategies corresponding to the N actions available
    in the symmetric game
  - There are M mixed strategies being used by agents in the population

Parameters
----------

pop_state : array-like
    A 1-dimensional array-like object of length M with element i being a
    numeric value between 0 and 1 specifying the proportion of the population
    playing mixed strategy i.  The values in the sequence must sum to 1.

strat_profile : array-like
    An M x N array-like object that specifies the mixed strategy profile for
    the population.  Each row i corresponds to a mixed strategy and each
    column j corresponds to a pure strategy that specifies a specific action
    in the game.  Therefore, an entry [i,j] specifies the probability that
    pure strategy j will be used by a player using mixed strategy i.  The
    values in each row i must sum to 1.

payoff_func : array-like
    An N x N array-like object that provides the payoffs for a player given
    the pure strategies that are selected by each player.  Since the game is
    assumed to be symmetric, the same array can be used by all players.

Returns
-------
pop_state : array-like
    The new population state after the population has evolved according to the
    specified evolutionary dynamics
'''
def rep_dynamics_2ss(pop_state, strat_profile, payoff_func):
    # TODO: check sizs of inputs
    # calculate the expected payoff for a mixed strategy i
    for i in range(sizpayoff_func)
    mstrat_i = strat_profile[i] # probabilities for each pure strategy

    # - probability of playing pure strategy j
    # - probability opponent is playing pure strategy k
    # - payoff when playing strategy j versus strategy k

'''
Verifies that the specified arrays are compatible with each other by
verifying the following conditions:
  - len(pop_state)
  - 
'''
def _check_arrays(pop_state, strat_profile, payoff_func):
    wrong_dim_msg = "{0} must be a 1-dim array - provided {1}-dim array"
    if (len(pop_state.shape) != 1):
        raise ValueError(wrong_dim_msg.format("pop_state", len(pop_state.shape)))
    M = pop_state.shape[0]

    if (len(strat_profile.shape) != 2):
        raise ValueError(wrong_dim_msg.format("strat_profile", len(strat_profile.shape)))

    wrong_size_msg = "Length of pop_state ({0}) doesn't match " +\
                     "number of rows in strat_profile ({1})"
    if (strat_profile.shape[0] != M):
        raise ValueError(wrong_size_msg(M, strat_profile.shape[0]))

    N = strat_profile.shape[1]

    if (len(payoff_func.shape) != 2):
        raise ValueError(wrong_dim_msg.format("payoff_func", len(payoff_func.shape)))

    wrong_size_msg = "Size of payoff_func ({0}) is not compatble with " +\
                     "number of rows in strat_profile ({1})"
    if ((payoff_func.shape[0] != N) or (payoff_func.shape[1] != N)):
        raise ValueError(wrong_size_msg.format(payoff_func.shape, N)


        





payoff
  
Replicator dynamics
'''
class ReplicatorDynamics:
    '''
    An implementation of the discrete replicator dynamics.
    Evolves the specified population into a new population.  The
    population provided to the method is not modified (??).
    '''
    def evolve(self, population):
        # calculate fitnesses for all agents using fitness_score function
        # -- use payoff as the fitness score by default

        # randomly select an agent to reproduce based on fitness
        # -- generate a random number and then find the selected agent
        # ri = RNGEN.randint(0, self.total_payouts);
        # thresh = 0;
        # for a in self.agents:
        #     thresh += a.payout
        #     if (ri <= thresh):
        #         return a;

        # radomly select an agent to eliminate using uniform distribution
        