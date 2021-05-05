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
is used.  Note that a pure strategy can be represented as a mixed stratgy
where one component is equal to one and the remaining components are equal
zero.

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

The pure-strategy payoff function :math:`\pi_i(\boldsymbol{s})` for
a game defines the payoff for player position :math:`\mathit{i}` when a
pure strategy profile :math:`\boldsymbol{s} \in \mathcal{S}` is in effect.
A mixed strategy profile :math:`\boldsymbol{\chi}` defines the probabilty
that each pure strategy profile :math:`\boldsymbol{s}` is in effect.
Therefore, the value of the pure-strategy payoff function
:math:`\pi_i(\boldsymbol{s})` cannot be deteremined when mixed strategy
:math:`\boldsymbol{\chi}` is in effect.

The `mixed-strategy payoff function` :math:`u_i(\boldsymbol{\chi})` for
player :math:`\mathit{i}` is defined as the `expected value` over all
pure-strategy profiles :math:`\boldsymbol{s} \in \mathcal{S}` of the
pure-strategy payoff function :math:`\pi_i(\boldsymbol{s})` given that mixed
strategy profile :math:`\boldsymbol{\chi}` is in effect:

.. math::

   \mathop{\mathbb{E}}\limits_{\boldsymbol{s} \in \mathcal{S}}
   [\pi_i(\boldsymbol{s})\mid\boldsymbol{\chi}]=
   \sum_{\boldsymbol{s} \in \mathcal{S}}
   \Pr(\boldsymbol{s}\mid\boldsymbol{\chi})
   \pi_i(\boldsymbol{s})

Example
-------
The following defines a possible mixed strategy profile for the game defined
in the previous example:

.. math::

   \boldsymbol{x_1}&=(0.65,0.35) \\
   \boldsymbol{x_2}&=(0.25,0.15,0.6) \\
   \boldsymbol{x_3}&=(0.25,0.05,0.2,0.5) \\
   \boldsymbol{\chi}&=(\boldsymbol{x_1},\boldsymbol{x_2},\boldsymbol{x_3})

In this case, the probability that the example pure strategy profile
:math:`\boldsymbol{s}=(1,3,4)` will be used is the following:

.. math::

  \Pr(\boldsymbol{s}\mid\boldsymbol{\chi})=
  \prod_{i=1}^{3} x_{i,s_i}=
  x_{1,1} \cdot x_{2,3} \cdot x_{3,4}=
  0.65 \cdot 0.6 \cdot 0.5=0.195

----------------------------------------------
2-Player Normal Form Games wit Pure Strategies
----------------------------------------------

In the special case of a game with only two player positions where position
one has :math:`m_1` pure strategies and position to has :math:`m_2` pure
strategies, the payoff functions can be defined using a pair of
:math:`m_1 \times m_2` matrices :math:`(\boldsymbol{A},\boldsymbol{B})`.

For all pure strategy profiles :math:`\boldsymbol{s}=(h,k)` where 
:math:`h \in \mathcal{S}_1` and :math:`k \in \mathcal{S}_2`, the two
payoff functions :math:`\pi_1(\boldsymbol{s})` and :math:`\pi_2(\boldsymbol{s})`
can be defined using the two matrices :math:`\boldsymbol{A}` and
:math:`\boldsymbol{B}` as follows:

.. math::

  \pi_1(\boldsymbol{s})=a_{h,k} \\
  \pi_2(\boldsymbol{s})=b_{h,k}

Note that a row in either matrix always corresponds to a pure strategy for
player position one and a columns always corresponds to a pure strategy for
player position two.

Example
-------

Consider the two player game created by removing player position three from
the game presented in the first example above:

.. math::

   \mathcal{I}&=\{1,2\} \\
   \mathcal{S}_1&=\{1,2\},\mathcal{S}_2=\{1,2,3\}

Let the payoff functions for the two player positions be defined by the
following :math:`2 \times 3` matrices:

.. math::

   \boldsymbol{A}&=\begin{pmatrix} 1 & 2 & 5 \\ 3 & 4 & 0 \end{pmatrix} \\
   \boldsymbol{B}&=\begin{pmatrix} 4 & 3 & 0\\ 2 & 1 & 2 \end{pmatrix}

Given the pure-strategy profile :math:`\boldsymbol{s}=(1,3)`, the payoffs for
the two player positions are the following:

.. math::

   \pi_1(\boldsymbol{s}) = a_{1,3} = 5 \\
   \pi_2(\boldsymbol{s}) = b_{1,3} = 0

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
