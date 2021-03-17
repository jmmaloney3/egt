# -*- coding: utf-8 -*-
"""
A module that provides implementations for common versions of
evolutionary dynamics.

Created on Sun Mar 07 21:35 2021

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
    The sum of the elements in x must equal 1.

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
    # np.dot(x, f) = average fitness for the population
    return x*(f / np.dot(x, f))