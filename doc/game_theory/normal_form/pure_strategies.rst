.. title:: Normal Form Games with Pure Strategies

.. _pure_strategies:

Normal Form Games with Pure Strategies
======================================

Let :math:`\mathcal{I}=\{1,2,\dots,n\}` be the set of `player positions` for a
`normal form` game.

Each player position :math:`\mathit{i}` has a set
:math:`\mathcal{S}_i=\{1,2,\dots,m_i\}` of `pure strategies`.  A `pure-strategy
profile`

.. math::

   \boldsymbol{s}=(s_1,s_2,\dots,s_n)

where :math:`s_i \in \mathcal{S}_i` represents a game configuration in which each
player position :math:`\mathit{i}` has chosen (or been assigned) a specific
pure strategy.  The set :math:`\mathcal{S}` of all possible pure-strategy
profiles is the `pure-strategy space` of the game.

A `pure-strategy payoff function` :math:`\pi_i(\boldsymbol{s})`
defines the payoff for player :math:`\mathit{i}` in the game configuration
specified by pure-strategy profile :math:`\boldsymbol{s}`.  The `combined
pure-strategy payoff function` :math:`\boldsymbol{\pi}(\boldsymbol{s})=
(\pi_1(\boldsymbol{s}),\pi_2(\boldsymbol{s}),\dots,\pi_n(\boldsymbol{s}))`
provides a vector representing the payoffs for each player position for
pure-strategy profile :math:`\boldsymbol{s}`.

Given these definitions, a game in normal form can be represented as the tuplet
:math:`\mathcal{G}=(\mathcal{I},\mathcal{S},\boldsymbol{\pi})`.

Example
-------
A game with three player positions where position one has two pure strategies,
position two has three pure strategies and position three has four pure
strategies has the following representation:

.. math::

   \mathcal{I}&=\{1,2,3\} \\
   \mathcal{S}_1&=\{1,2\},\mathcal{S}_2=\{1,2,3\},\mathcal{S}_3=\{1,2,3,4\} \\
   \mathcal{S}&=\mathcal{S}_1\times\mathcal{S}_2\times\mathcal{S}_3=\left\{
   \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix},
   \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix},
   \dots
   \begin{pmatrix} 2 \\ 3 \\ 3 \end{pmatrix},
   \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}
   \right\}

For this example game, the following defines a possible pure strategy profile
for the game:

.. math::

   \boldsymbol{s}=(1,3,4)

