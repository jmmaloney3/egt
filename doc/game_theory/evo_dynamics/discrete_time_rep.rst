.. title:: Discrete Time Replictor Dynamics

.. _evo_dynamics_discrete_tme_rep:

Discrete Time Replicator Dynamics
=================================

Let :math:`\mathcal{G}` be a symmetric two-player game with :math:`m` pure
strategies that is the `stage game` for an `evolutionary game` played by an
infinite population :math:`\mathcal{A}` of agents.  Assume that the population
of agents plays the game repeatedly over time periods
:math:`\mathit{t} = 1, 2, \dots`. At the end of each time period, the
population evolves so that the percentage of the population playing strategy
:math:`\boldsymbol{x}_k` increases if the expected payout :math:`\mathit{u}_k`
for that strategy is greater than the population average payout
:math:`\bar{u}_{\boldsymbol{\sigma}}` and decreases otherwise.

The `discrete time replicator dynamics` are frequenty used to determine how
a population evolves after each time step.  For each strategy, the proporation
of the population using that stragegy is changed by an amount equal to the
percentage of the population average payout achieved by the strategy's
expected payout.

The change in the proportion of the population playing strategy
:math:`\mathit{k}`, is equal to:

.. math::
   \Delta_{\sigma_k} = \frac{\mathit{u}_k}{\bar{u}_{\boldsymbol{\sigma}}}

Therefore, the proportion of the population using strategy :math:`{\mathit{k}}`
at time step :math:`\mathit{t}+1` is equal to:

.. math::
   \sigma_{k,t+1} = \Delta_{\sigma_k,t} \cdot \sigma_{k,t}
                  = \frac{\mathit{u}_{k,t}}{\bar{u}_{\boldsymbol{\sigma},t}}
                    \cdot \sigma_{k,t}

Example
-------

TBD
