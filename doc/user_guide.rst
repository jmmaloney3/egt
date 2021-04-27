.. title:: User guide : contents

.. _user_guide:

==================================================
User Guide: Evolutionary Game Theory (EGT) Toolkit
==================================================

--------------------------------------
Normal Form Games with Pure Strategies
--------------------------------------

Let :math:`\mathcal{I}=\{1,2,\dots,n\}` be the set of `player positions` for a
`normal form` game.

Each player position :math:`\mathit{i}` has a set
:math:`\mathcal{S}_i=\{1,2,\dots,m_i\}` of `pure strategies`.  A `pure-strategy
profile` :math:`\boldsymbol{s}=(s_1,s_2,\dots,s_n)` represents a game
configuration in which each player position :math:`\mathit{i}` has chosen
(or been assigned) a specific pure strategy :math:`s_i \in S_i`.  The set
:math:`\mathcal{S}` of all possible pure-strategy profiles is the
`pure-strategy space` of the game.

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

---------------------------------------
Normal Form Games with Mixed Strategies
---------------------------------------

A `mixed strategy` for player positon :math:`i \in \mathcal{I}` is a vector
:math:`\boldsymbol{x_i}=(x_{i,1},x_{i,2},\dots,x_{i,m_i})` where for
:math:`h \in \mathcal{S}_i`

.. math::

      x_{i,h} = \Pr(h \mid \boldsymbol{x_i})

This is the probability that player position :math:`\mathit{i}` plays
pure strategy :math:`\mathit{h}` when mixed strategy :math:`\boldsymbol{x_i}`
is used.

A `mixed strategy profile` :math:`\boldsymbol{\chi}=(\boldsymbol{x_1},
\boldsymbol{x_2},\dots,\boldsymbol{x_n})` is a game configuration
in which each player position :math:`\mathit{i}` has been assigned a mixed
strategy :math:`\boldsymbol{x_i}`.

The probability that a pure strategy profile :math:`\boldsymbol{s}` will be
played when a mixed strategy profile :math:`\boldsymbol{\chi}` is in effect
is equal to the following:

.. math::

   \Pr(\boldsymbol{s}\mid\boldsymbol{\chi})=\prod_{i=1}^{n} x_{i,s_i}

Where :math:`s_i \in \mathcal{S}_i` is the pure strategy for position
:math:`\mathit{i}` specified by pure strategy profile :math:`\boldsymbol{s}`
and

.. math::

   x_{i,s_i} = \Pr(s_i \mid \boldsymbol{x_i})

------------------------
Symmetric 2-Player Games
------------------------

The ``egt`` package currently supports the use of `2-person symmetric` games
as the `stage game` for simulations.  In this case, the number of player
positions is limited to two and each player position has the same set of pure
strategies.

.. math::

   I &= \{1,2\} \\
   S_1 &= S_2 = \{1,2,\dots,m\}

In addition, given strategy profile :math:`s_a=(s_1,s_2)` and a second strategy
profile :math:`s_b=(s_2,s_1)` where the pure strategies assigned to each player
position have been swapped, the payoff functions for the two player positions
satisfy the following conditions:

.. math::

   \pi_1(s_a) &= \pi_2(s_b) \\
   \pi_1(s_b) &= \pi_2(s_a)

:math:`s_1,s_2 \in S_1=S_2`, the following is true for the payoff functions the two
player positions conforms to the following
   \pi = (\pi_1,\pi_2)



Since the game is `symmetric`, the game's `payoffs` can be represented by a
single matrix ``A`` that specifies the payoffs for `player one`.  The payoffs
for `player two` are provided by the transpose of matrix ``A``.

For a `stage game` with ``m`` `pure strategies`, a `mixed strategy` is
represented by a ``m``-vector whose ``i``-th component specifies the
probability that the agent will play the ``i``-th `pure strategy`.

Given two agents playing mixed strategies ``x`` and ``y``, the `expected payoffs`
``u`` for the two agents are given by the following equations:

.. math::

   u(x,y) &= \sum_{h=1}^{m}\sum_{k=1}^{m}x_{h}\cdot a_{h,k}\cdot y_{k} = xAy \\
   u(y,x) &= \sum_{k=1}^{m}\sum_{h=1}^{m}y_{k}\cdot a_{k,h}\cdot x_{h} = yAx = xA^Ty

------------------
Evolutionary Games
------------------

A `strategy profile` for a population of agents playing ``n`` different mixed
stategies is represented by a ``n`` x ``m`` matrix whose ``j``-th row
represents the mixed strategy for the ``j``-th agent type.

A `population state` for an infinite population of agents playing ``n``
different mixed strategies is represented by a ``n``-vector whose ``j``-th
component represents the proportion of the population playing the ``j``-th
mixed strategy in the population's `strategy profile`.

Given a `strategy profile` matrix ``X``, a `population state` vector ``p``,
and a `well-mixed` population of agents, the probability that an agent
encounters another agent playing the ``i``-th pure strategy is given by the
following equation:

.. math::

   P_i(X,p) = \sum_{j=1}^{n}p_{j}x_{j,i}

The ``m``-vector specifing the probabilities that an agent encounters another
agent playing any one of the ``m`` pure strategies is given by the following
matrix equation:

.. math::

   P(X,p) = pX

The vector ``P`` is identical to a `mixed strategy`.  Therefore, the `expected
payoff` for an agent playing the ``j``-th `mixed strategy` is given by the 
following equation:

.. math::

    u(x_j,P) = \sum_{h=1}^{m}\sum_{k=1}^{m}x_{j,h}\cdot a_{h,k}\cdot P_{k} = x_jAP

The ``n``-vector specifying the the `expected payoffs` for all ``n`` agent
types is given by the following matrix equation:

.. math::

   U(X,p) = XApX = XAP
