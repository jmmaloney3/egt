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
:math:`\boldsymbol{x}_i=(x_{i,1},x_{i,2},\dots,x_{i,m_i})` where for
:math:`h \in \mathcal{S}_i`

.. math::

      x_{i,h} = \Pr(h \mid \boldsymbol{x}_i)

This is the probability that player position :math:`\mathit{i}` plays
pure strategy :math:`\mathit{h}` when mixed strategy :math:`\boldsymbol{x}_i`
is used.

The pure strategy :math:`\mathit{h}` for player position :math:`\mathit{i}`
can be represented as a mixed stratgy :math:`\boldsymbol{e}_{i,h}` that
assigns probability one to pure strategy :math:`\mathit{h}` and zero
probability to all other pure strategies.

.. math::

   \Pr(\mathit{h} &\mid \boldsymbol{e}_{i,h}) = 1 \\
   \Pr(\mathit{k} &\mid \boldsymbol{e}_{i,h} \land \mathit{k}\neq\mathit{h})=0

A `mixed strategy profile` :math:`\boldsymbol{\chi}=(\boldsymbol{x}_1,
\boldsymbol{x}_2,\dots,\boldsymbol{x}_n)` is a game configuration
in which each player position :math:`\mathit{i}` has been assigned a mixed
strategy :math:`\boldsymbol{x}_i`.

The probability that a pure strategy profile :math:`\boldsymbol{s}` will be
played when a mixed strategy profile :math:`\boldsymbol{\chi}` is in effect
is equal to the following:

.. math::

   \Pr(\boldsymbol{s}\mid\boldsymbol{\chi})=\prod_{i=1}^{n} x_{i,s_i}

Where :math:`s_i \in \mathcal{S}_i` is the pure strategy for position
:math:`\mathit{i}` specified by pure strategy profile :math:`\boldsymbol{s}`
and

.. math::

   x_{i,s_i} = \Pr(s_i \mid \boldsymbol{x}_i)

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

   u_i(\boldsymbol{\chi})= \
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
   \boldsymbol{\chi}&=(\boldsymbol{x}_1,\boldsymbol{x}_2,\boldsymbol{x}_3)

In this case, the probability that the example pure strategy profile
:math:`\boldsymbol{s}=(1,3,4)` will be used is the following:

.. math::

  \Pr(\boldsymbol{s}\mid\boldsymbol{\chi})=
  \prod_{i=1}^{3} x_{i,s_i}=
  x_{1,1} \cdot x_{2,3} \cdot x_{3,4}=
  0.65 \cdot 0.6 \cdot 0.5=0.195

--------------------------
2-Player Normal Form Games
--------------------------

In the special case of a game with only two player positions where position
one has :math:`m_1` pure strategies and position two has :math:`m_2` pure
strategies, the payoff functions can be defined using a pair of
:math:`m_1 \times m_2` `payoff matrices`
:math:`(\boldsymbol{A},\boldsymbol{B})`.

For all pure strategy profiles :math:`\boldsymbol{s}_{h,k}=(h,k)` where 
:math:`h \in \mathcal{S}_1` and :math:`k \in \mathcal{S}_2`, the two
pure strategy payoff functions :math:`\pi_1(\boldsymbol{s}_{h,k})` and
:math:`\pi_2(\boldsymbol{s}_{h,k})` can be defined using the two matrices
:math:`\boldsymbol{A}` and :math:`\boldsymbol{B}` as follows:

.. math::

  \pi_1(\boldsymbol{s}_{h,k})=a_{h,k} \\
  \pi_2(\boldsymbol{s}_{h,k})=b_{h,k}

Note that a row in either matrix always corresponds to a pure strategy for
player position one and a column always corresponds to a pure strategy for
player position two.

For all mixed-strategy profiles
:math:`\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}}=
(\boldsymbol{x},\boldsymbol{y})` where :math:`\boldsymbol{x}` is a mixed
stratgy for player position one and :math:`\boldsymbol{y}` is a mixed strategy
for player position two, the two mixed strategy payoff functions
:math:`u_1(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})` and
:math:`u_2(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})` can also
be defined using the two matrices as follows:

.. math::

  u_1(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})&= 
  \sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  \Pr(\boldsymbol{s_{h,k}}\mid\boldsymbol{\chi}_
  {\boldsymbol{x},\boldsymbol{y}})
  \pi_1(\boldsymbol{s_{h,k}}) \\
  &=\sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  (x_h \cdot y_k) a_{h,k} \\
  &=\sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  x_h \cdot a_{h,k} \cdot y_k \\
  &=\boldsymbol{x} \boldsymbol{A} \boldsymbol{y}

  u_2(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})&= 
  \sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  \Pr(\boldsymbol{s_{h,k}}\mid\boldsymbol{\chi}_
  {\boldsymbol{x},\boldsymbol{y}})
  \pi_2(\boldsymbol{s_{h,k}}) \\
  &=\sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  (x_h \cdot y_k) b_{h,k} \\
  &=\sum_{h \in \mathcal{S}_1, k \in \mathcal{S}_2}
  x_h \cdot b_{h,k} \cdot y_k \\
  &=\boldsymbol{x} \boldsymbol{B} \boldsymbol{y}
  =\boldsymbol{y} \boldsymbol{B}^T \boldsymbol{x}

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

Given the pure-strategy profile :math:`\boldsymbol{s}=(1,3)`, the
pure-strategy payoffs for the two player positions are the following:

.. math::

   \pi_1(\boldsymbol{s}) = a_{1,3} = 5 \\
   \pi_2(\boldsymbol{s}) = b_{1,3} = 0

Given the mixed-strategy profile
:math:`\boldsymbol{\chi}=(\boldsymbol{x}_1,\boldsymbol{x}_2)` where

.. math::

   \boldsymbol{x}_1&=(0.65,0.35) \\
   \boldsymbol{x}_2&=(0.25,0.15,0.6)

the mixed-strategy payouts for the two player positions are the following:

.. math::

   u_1(\boldsymbol{\chi})=&\boldsymbol{x}_1\boldsymbol{A}\boldsymbol{x}_2 \\
   =&(0.65 \cdot 1 \cdot 0.25) +
     (0.65 \cdot 2 \cdot 0.15) + 
     (0.65 \cdot 5 \cdot 0.6) + \\
   & (0.35 \cdot 3 \cdot 0.25) +
     (0.35 \cdot 4 \cdot 0.15) + 
     (0.35 \cdot 0 \cdot 0.6) \\
   =&2.78

   u_2(\boldsymbol{\chi})=&\boldsymbol{x}_1\boldsymbol{B}\boldsymbol{x}_2 \\
   =&(0.65 \cdot 4 \cdot 0.25) +
     (0.65 \cdot 3 \cdot 0.15) + 
     (0.65 \cdot 0 \cdot 0.6) + \\
   & (0.35 \cdot 2 \cdot 0.25) +
     (0.35 \cdot 1 \cdot 0.15) + 
     (0.35 \cdot 2 \cdot 0.6) \\
   =&1.59

------------------------------------
Symmetric 2-Player Normal Form Games
------------------------------------

In the special case of a `symmetric` two-player normal form game, each player
position has :math:`m` pure strategies and the pair of :math:`m \times m`
payoff matrices :math:`(\boldsymbol{A},\boldsymbol{B})` meets the following
aditional requirement:

.. math::

   \boldsymbol{B} = \boldsymbol{A}^T

This implies that the payoff accrued by a pure strategy is independent of the
player position that plays that strategy.   Therefore, for all
:math:`h,k \in \mathcal{S}=\mathcal{S}_1=\mathcal{S}_2`, given two pure
strategy profiles :math:`\boldsymbol{s}_{h,k}=(h,k)` and
:math:`\boldsymbol{s}_{k,h}=(k,h)` that are identical except that the pure
strategies assigned to each player position have been swapped, the pure
strategy payoff functions for the two player positions satisfy the following
conditions:

.. math::

   \pi_1(\boldsymbol{s}_{h,k}) &= \pi_2(\boldsymbol{s}_{k,h}) \\
   \pi_1(\boldsymbol{s}_{k,h}) &= \pi_2(\boldsymbol{s}_{h,k})

Since :math:`\boldsymbol{B} = \boldsymbol{A}^T` in the case of a symmetric
two person game, the two pure strategy payoff functions
:math:`\pi_1(\boldsymbol{s}_{h,k})` and :math:`\pi_2(\boldsymbol{s}_{h,k})`
can be defined using a single matrix :math:`\boldsymbol{A}` as follows:

.. math::

   \pi_1(\boldsymbol{s}_{h,k})=a_{h,k} \\
   \pi_2(\boldsymbol{s}_{h,k})=a_{k,h}
 
Note that the order of the indices used to select the element from matrix
:math:`\boldsymbol{A}` for :math:`\pi_2` is the reverse of the order of the
indices used for :math:`\pi_1`.

Using the definitions given above for the two pure strategy payoff functions
for a symmetric two player game, the two mixed strategy payoff functions
:math:`u_1(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})` and
:math:`u_2(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})` can be
defined as follows:

.. math::

   u_1(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})&=
   \boldsymbol{x} \boldsymbol{A} \boldsymbol{y}

   u_2(\boldsymbol{\chi}_{\boldsymbol{x},\boldsymbol{y}})&=
   \boldsymbol{x} \boldsymbol{A}^T \boldsymbol{y}=
   \boldsymbol{y} \boldsymbol{A} \boldsymbol{x}

Example
-------
Consider the `prisoner's dilemma`, a symmetric two player game with two
pure strategies, `cooperate` and `defect`, and the following generalized
payout matrix :math:`\boldsymbol{A}`:

.. math::

   \boldsymbol{A}&=\begin{pmatrix} R & S \\ T & P \end{pmatrix}  \\
   \boldsymbol{A}^T&=\begin{pmatrix} R & T \\ S & P \end{pmatrix}

where the payouts satisfy the following condition:

.. math::

   \mathit{T} > \mathit{R} > \mathit{P} > \mathit{S}

Consider a specific case that uses the following payout matrix:

.. math::

   \boldsymbol{A}=\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}

Given the pure-strategy profile :math:`\boldsymbol{s}=(1,2)`, the
pure-strategy payoffs for the two strategies are the following:

.. math::

   \pi_1(\boldsymbol{s}) = a_{1,2} = 0 \\
   \pi_2(\boldsymbol{s}) = a_{2,1} = 5

Given the mixed-strategy profile
:math:`\boldsymbol{\chi}=(\boldsymbol{x}_1,\boldsymbol{x}_2)` where

.. math::

   \boldsymbol{x}_1&=(0.65,0.35) \\
   \boldsymbol{x}_2&=(0.25,0.75)

the mixed-strategy payouts for the two strategies are the following:

.. math::

   u_1(\boldsymbol{\chi})=&\boldsymbol{x}_1\boldsymbol{A}\boldsymbol{x}_2 \\
   =&(0.65 \cdot 3 \cdot 0.25) +
     (0.65 \cdot 0 \cdot 0.75) + \\
   & (0.35 \cdot 5 \cdot 0.25) +
     (0.35 \cdot 1 \cdot 0.75)   \\
   =&1.15

   u_2(\boldsymbol{\chi})=&\boldsymbol{x}_1\boldsymbol{A}^T\boldsymbol{x}_2 \\
   =&(0.65 \cdot 3 \cdot 0.25) +
     (0.65 \cdot 5 \cdot 0.75) + \\
   & (0.35 \cdot 0 \cdot 0.25) +
     (0.35 \cdot 1 \cdot 0.75)   \\
   =&3.15

---------------------------------------
Evolutionary Games with Pure Strategies
---------------------------------------

Let :math:`\mathcal{G}` be a symmetric two-player game with :math:`m` pure
strategies.  Assume there is a `well-mixed` infinite population
:math:`\mathcal{A}` of agents and that pairs of agents are repeatedly drawn at
random to play the `stage game` :math:`\mathcal{G}`. Each agent is assigned
one of :math:`m` `pure-strategy types`.  The agent's type determines the pure
strategy that the agent will use when it plays the game.

A `population pure-strategy profile` is a :math:`m \times m` identity matrix
:math:`\boldsymbol{S}` whose columns are the :math:`\mathit{m}` mixed 
strategies :math:`\boldsymbol{e}_h` representing the :math:`\mathit{m}` pure
strategies played by the agents in the population - column :math:`\mathit{h}`
defines mixed strategy :math:`\boldsymbol{e}_h`.


.. math::

   \boldsymbol{S}=
   (\boldsymbol{e}_1 \hdots \boldsymbol{e}_h \hdots \boldsymbol{e}_m)=
   \begin{pmatrix}
   1 & \hdots & 0 & \hdots & 0 \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   0 & \hdots & 1 & \hdots & 0 \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   0 & \hdots & 0 & \hdots & 1 \\
   \end{pmatrix}

A `pure-strategy population state` is a vector
:math:`\boldsymbol{\sigma}=(\sigma_1,\sigma_2,\dots,\sigma_m)` where each
:math:`\sigma_h` defines the proportion of the agent population assigned to
pure strategy type :math:`h`.

When an agent is selected at random from the population, the probability that
the agent will play pure strategy :math:`h` is equal to:

.. math::

   \sigma_h = \Pr(h \mid \boldsymbol{\sigma})

This is equivalent to the probability that a single agent using
mixed-strategy :math:`\boldsymbol{\sigma}` will play pure strategy :math:`h`.

Given payout matrix :math:`\boldsymbol{A}`, the expected payout for an agent
playing pure strategy :math:`\boldsymbol{e}_h` against an agent that is
randomly selected from a population in state :math:`\boldsymbol{\sigma}` is
equivalent to the expected payout for the same agent playing against an agent
that is using mixed-strategy :math:`\boldsymbol{\sigma}`.

.. math::

   u_h = \boldsymbol{e}_h\boldsymbol{A}\boldsymbol{\sigma}

Replacing the vector :math:`\boldsymbol{e}_h` with the population pure-strategy
profile matrix :math:`\boldsymbol{S}` in the previous equation provides a
matrix equation that generates the vector :math:`\boldsymbol{u}` of expected
payouts for all pure strategy types:

.. math::

   \boldsymbol{u} = (u_1, u_2, \dots, u_m) = 
   \boldsymbol{S}\boldsymbol{A}\boldsymbol{\sigma}

The `population average payout` is the expected payout earned by
one randomly selected agent playing against a second randomly selected agent.
Since two agents selected randomly from the population to play a game can
equivelently be treated as two agents that are both playing mixed-strategy
:math:`\boldsymbol{\sigma}`, the population average payout is equal to the
mixed-strategy payout when mixed strategy profile
:math:`(\boldsymbol{\sigma},\boldsymbol{\sigma})` is in effect.

.. math::

   \bar{u}_{\boldsymbol{\sigma}}=
   \mathop{\mathbb{E}}\limits_{\boldsymbol{a} \in \mathcal{A}}
   [\mathit{u}_a \mid \boldsymbol{\sigma}]=
   \boldsymbol{\sigma}\boldsymbol{A}\boldsymbol{\sigma}

Example
-------

Consider the case where a population of agents is playing the prisoner's
dilemma game presented in the previous example.  By definition, the population
pure-strategy profile is given by the :math:`2 \times 2` identify matrix:

.. math::

   \boldsymbol{S} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}

Assume that the following population state vector :math:`\boldsymbol{\sigma}`
specifies how the population is distributed among the two strategies:

.. math::

   \boldsymbol{\sigma} = (0.25, 0.75)

The expected payouts for the two pure-strategy types are the following:

.. math::

   u_1 =& \boldsymbol{e}_1\boldsymbol{A}\boldsymbol{\sigma} \\
   =&(1 \cdot 3 \cdot 0.25) +
     (1 \cdot 0 \cdot 0.75) + \\
   & (0 \cdot 5 \cdot 0.25) +
     (0 \cdot 1 \cdot 0.75)   \\
   =&0.75

   u_2 =& \boldsymbol{e}_2\boldsymbol{A}\boldsymbol{\sigma} \\
   =&(0 \cdot 3 \cdot 0.25) +
     (0 \cdot 0 \cdot 0.75) + \\
   & (1 \cdot 5 \cdot 0.25) +
     (1 \cdot 1 \cdot 0.75)   \\
   =&2.00

The population average payout is equal to the following:

.. math::

   \bar{u}_{\boldsymbol{\sigma}}
   =&\boldsymbol{\sigma}\boldsymbol{A}\boldsymbol{\sigma} \\
   =&(0.25 \cdot 3 \cdot 0.25) +
     (0.25 \cdot 0 \cdot 0.75) + \\
   & (0.75 \cdot 5 \cdot 0.25) +
     (0.75 \cdot 1 \cdot 0.75)   \\
   =&(0.25 \cdot u_1) + (0.75 \cdot u_2) \\
   =&1.6875

----------------------------------------
Evolutionary Games with Mixed Strategies
----------------------------------------

Let :math:`\mathcal{G}` be a symmetric two-player game with :math:`m` pure
strategies.  Assume there is a `well-mixed` infinite population
:math:`\mathcal{A}` of agents and that pairs of agents are repeatedly drawn at
random to play the `stage game` :math:`\mathcal{G}`. Also assume that there
are :math:`\mathit{n}` agent types each using a different mixed strategy
:math:`\boldsymbol{x}_k`.

A `population mixed-strategy profile` is a :math:`m \times n` matrix
:math:`\boldsymbol{X}` whose columns define the :math:`\mathit{n}` mixed 
strategies played by the agents in the population - column :math:`\mathit{k}`
defines mixed strategy :math:`\boldsymbol{x}_k`.

.. math::

   \boldsymbol{X}=
   \begin{pmatrix}
   x_{1,1} & \hdots & x_{k,1} & \hdots & x_{n,1} \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   x_{1,h} & \hdots & x_{k,h} & \hdots & x_{n,h} \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   x_{1,m} & \hdots & x_{k,m} & \hdots & x_{n,m} \\
   \end{pmatrix}

A `mixed-strategy population state` is a vector
:math:`\boldsymbol{\sigma}=(\sigma_1,\sigma_2,\dots,\sigma_n)` where each
:math:`\sigma_k` defines the proportion of the agent population assigned to
mixed strategy :math:`\boldsymbol{x}_k`.

When an agent is selected at random from the population, the probability that
the agent will play mixed strategy :math:`\boldsymbol{x}_k` is equal to:

.. math::

   \sigma_{\boldsymbol{x}_k} = \Pr(\boldsymbol{x}_k \mid \boldsymbol{\sigma})

The probability that the randomly selected agent will play pure strategy
:math:`\mathit{h}` is equal to:

.. math::

   \Pr(h \mid \boldsymbol{\sigma})
   &= \sum_{k=1}^n{\Pr(h \mid \boldsymbol{x}_k)
                  \Pr(\boldsymbol{x}_k \mid \boldsymbol{\sigma})} \\
   &= \sum_{k=1}^n{x_{k,h} \cdot \sigma_k}

This is equivalent to the probability that a single agent using
the `population mixed-strategy` :math:`\boldsymbol{x}_{\boldsymbol{\sigma}}`
will play pure strategy :math:`h`.

.. math::

   \boldsymbol{x}_{\boldsymbol{\sigma}}=\boldsymbol{X}\boldsymbol{\sigma}

Given payout matrix :math:`\boldsymbol{A}`, the expected payout for an agent
playing mixed strategy :math:`\boldsymbol{x}_k` against an agent that is
randomly selected from a population in state :math:`\boldsymbol{\sigma}` is
equivalent to the expected payout for the same agent playing against an agent
that is using population mixed-strategy
:math:`\boldsymbol{x}_{\boldsymbol{\sigma}}`.

.. math::

   u_{\boldsymbol{x}_k} =
   \boldsymbol{x}_k\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}

Replacing the vector :math:`\boldsymbol{x}_k` with the population
mixed-strategy profile matrix :math:`\boldsymbol{X}` in the previous equation
provides a matrix equation that generates the vector :math:`\boldsymbol{u}` of
expected payouts for all mixed strategy types:

.. math::

   \boldsymbol{u} = (u_1, u_2, \dots, u_n) = 
   \boldsymbol{X}\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}

The `population average payout` is the expected payout earned by
one randomly selected agent playing against a second randomly selected agent.
Since two agents selected randomly from the population to play a game can
equivelently be treated as two agents that are both playing the population
mixed-strategy :math:`\boldsymbol{x}_{\boldsymbol{\sigma}}`, the population
average payout is equal to the mixed-strategy payout when mixed strategy profile
:math:`(\boldsymbol{x}_{\boldsymbol{\sigma}},\boldsymbol{x}_{\boldsymbol{\sigma}})`
is in effect.

.. math::

   \bar{u}_{\boldsymbol{\sigma}}=
   \mathop{\mathbb{E}}\limits_{\boldsymbol{a} \in \mathcal{A}}
   [\mathit{u}_a \mid \boldsymbol{x}_{\boldsymbol{\sigma}}]=
   \boldsymbol{x}_{\boldsymbol{\sigma}}\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}

Example
-------
Consider another case where a population of agents is playing the prisoner's
dilemma game presented in previous examples. In this case, assume that there
are three different agent types playing the following mixed strategies:

.. math::

   \boldsymbol{x}_1 = (0.25, 0.75) \\
   \boldsymbol{x}_2 = (0.50, 0.50) \\
   \boldsymbol{x}_3 = (0.75, 0.25)

The population mixed-strategy profile is given by the following
:math:`2 \times 3` matrix:

.. math::

   \boldsymbol{X} =
   \begin{pmatrix}
   0.25 & 0.5 & 0.75 \\
   0.75 & 0.5 & 0.25
   \end{pmatrix}

Assume that the following population state vector :math:`\boldsymbol{\sigma}`
specifies how the population is distributed among the three mixed strategies:

.. math::

   \boldsymbol{\sigma} = (0.2, 0.5, 0.3)

The population mixed-strategy :math:`\boldsymbol{x}_{\boldsymbol{\sigma}}`
is the following:

.. math::

   \boldsymbol{x}_{\boldsymbol{\sigma}}=&\boldsymbol{X}\boldsymbol{\sigma} \\
   =&
   \begin{pmatrix}0.25 & 0.5 & 0.75 \\ 0.75 & 0.5 & 0.25\end{pmatrix}
   \begin{pmatrix}0.2 \\ 0.5 \\ 0.3\end{pmatrix} \\
   =&
   \begin{pmatrix}0.525 \\ 0.475\end{pmatrix}

The expected payouts for the three mixed-strategy types are the following:

.. math::

   \boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}} =&
   \begin{pmatrix}3 & 0 \\ 5 & 1\end{pmatrix}
   \begin{pmatrix}0.525 \\ 0.475\end{pmatrix}
   =
   \begin{pmatrix}1.575 \\ 3.1\end{pmatrix}

   u_1 =& \boldsymbol{x}_1\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}
   =
   \begin{pmatrix}0.25 & 0.75\end{pmatrix}
   \begin{pmatrix}1.575 \\ 3.1\end{pmatrix}
   =2.71875
   
   u_2 =& \boldsymbol{x}_2\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}
   =
   \begin{pmatrix}0.50 & 0.50\end{pmatrix}
   \begin{pmatrix}1.575 \\ 3.1\end{pmatrix}
   =2.3375

   u_3 =& \boldsymbol{x}_3\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}
   =
   \begin{pmatrix}0.75 & 0.25\end{pmatrix}
   \begin{pmatrix}1.575 \\ 3.1\end{pmatrix}
   =1.95625

The population average payout is equal to the following:

.. math::

   \bar{u}_{\boldsymbol{\sigma}}
   =&\boldsymbol{x}_{\boldsymbol{\sigma}}\boldsymbol{A}
   \boldsymbol{x}_{\boldsymbol{\sigma}}
   =
   \begin{pmatrix}0.525 & 0.475\end{pmatrix}
   \begin{pmatrix}3 & 0 \\ 5 & 1\end{pmatrix}
   \begin{pmatrix}0.525 \\ 0.475\end{pmatrix} \\
   =&
   \begin{pmatrix}0.525 & 0.475\end{pmatrix}
   \begin{pmatrix}1.575 \\ 3.1\end{pmatrix}
   =2.299375

----------------------------------------------
Evolutionary Games with Pseudo-pure Strategies
----------------------------------------------
Let :math:`\mathcal{G}` be a symmetric two-player game with :math:`\mathit{m}`
pure strategies that is the `stage game` for an evolutionary game played by a
population of agents playing :math:`\mathit{n}` different mixed strategies.

The game can be transformed into a symmetric two-player game
:math:`\mathcal{G}^*` with `pseudo-pure` strategies corresponding to the
:math:`\mathit{n}` mixed strategies played by the different types of agents.

Let :math:`\boldsymbol{A}^*` be the `pseudo-pure strategy payout matrix` for
the transformed game :math:`\mathcal{G}^*`. The entry in row
:math:`\mathit{i}` and column :math:`\mathit{j}` of matrix
:math:`\boldsymbol{A}^*` is the expected payout when mixed-strategy profile
:math:`\boldsymbol{\chi}=(\boldsymbol{x}_i, \boldsymbol{x}_j)` is in effect.

.. math::

   \mathit{a}^*_{i,j} &=
   \mathop{\mathbb{E}}[\mathit{u}(\boldsymbol{\chi})
   \mid
   \boldsymbol{\chi}=(\boldsymbol{x}_i, \boldsymbol{x}_j)] \\
   &=\sum_{h=0}^m\sum_{k=0}^m x_{i,h} \cdot a_{h,k} \cdot x_{j,k} \\
   &=\boldsymbol{x}_i \boldsymbol{A} \boldsymbol{x}_j

Given the population mixed-strategy profile :math:`\boldsymbol{X}`, the
complete payout matrix :math:`\boldsymbol{A}^*` can be calculated as follows:

.. math::

   \boldsymbol{A}^* = \boldsymbol{X}^T\boldsymbol{A}\boldsymbol{X}

Given payout matrix :math:`\boldsymbol{A}^*`, the set of mixed strategies can
be treated as `pseudo-pure strategies` and the equations for `evolutionary
games with pure strategies` can be used to calculate the expected payouts
for each mixed-strategy type and the population average payout.

A `population pseudo-pure strategy profile` is a
:math:`\mathit{n} \times \mathit{n}` identity matrix :math:`\boldsymbol{S}^*`
whose columns are the :math:`\mathit{n}` pseudo-pure strategy vectors
:math:`\boldsymbol{e}_i^*` corresponding to the :math:`\mathit{n}` mixed
strategies played by the agents in the population.

.. math::
   \boldsymbol{S}^*=
   (\boldsymbol{e}_1^* \hdots \boldsymbol{e}_h^* \hdots \boldsymbol{e}_m^*)=
   \begin{pmatrix}
   1 & \hdots & 0 & \hdots & 0 \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   0 & \hdots & 1 & \hdots & 0 \\
   \vdots  & \vdots & \vdots  & \vdots & \vdots  \\
   0 & \hdots & 0 & \hdots & 1 \\
   \end{pmatrix}

Given mixed-strategy profile
:math:`\boldsymbol{\chi}=(\boldsymbol{x}_i,\boldsymbol{x}_j)`, the equivalent
`pseudo-pure strategy profile` is :math:`\boldsymbol{s}^*=(i,j)` and the
expected payout for mixed strategy :math:`\boldsymbol{x}_i` is the following:

.. math::

   \pi_i^*(\boldsymbol{s}^*) =
   \boldsymbol{e}_i^* \boldsymbol{A}^* \boldsymbol{e}_j^* = 
   \mathit{a}_{i,j}^* =
   \boldsymbol{x}_i \boldsymbol{A} \boldsymbol{x}_j =
   u_i(\boldsymbol{\chi})

In the context of the transformed game :math:`\mathcal{G}^*`, the
`pseudo-pure strategy population state` vector is equivalent to the
mixed-strategy population state vector :math:`\boldsymbol{\sigma}`.

The expected payout for an agent playing pseudo-pure strategy
:math:`\boldsymbol{e}_i^*` against an agent that is randomly selected from a
population in state :math:`\boldsymbol{\sigma}` is equivalent to the expected
payout for the same agent playing against an agent that is using population
mixed-strategy :math:`\boldsymbol{\sigma}`.

.. math::
   u_{\boldsymbol{x}_i} =\boldsymbol{e}_i^*\boldsymbol{A}^*\boldsymbol{\sigma}

Replacing the vector :math:`\boldsymbol{e}_i^*` with the population
pseudo-pure strategy profile :math:`\boldsymbol{S}^*` in the previous equation
provides a matrix equation that generates the vector :math:`\boldsymbol{u}` of
expected payouts for all pseudo-pure strategy types:

.. math::

   \boldsymbol{u} = (u_1, u_2, \dots, u_n) = 
   \boldsymbol{S}^*\boldsymbol{A}^*\boldsymbol{\sigma}

The `population average payout` is the expected payout earned by
one randomly selected agent playing against a second randomly selected agent.
Since two agents selected randomly from the population to play a game can
equivelently be treated as two agents that are both playing mixed-strategy
:math:`\boldsymbol{\sigma}`, the population average payout is equal to the
mixed-strategy payout when mixed strategy profile
:math:`(\boldsymbol{\sigma},\boldsymbol{\sigma})` is in effect.

.. math::

   \bar{u}_{\boldsymbol{\sigma}}=
   \mathop{\mathbb{E}}\limits_{\boldsymbol{a} \in \mathcal{A}}
   [\mathit{u}_a \mid \boldsymbol{\sigma}]=
   \boldsymbol{\sigma}\boldsymbol{A}^*\boldsymbol{\sigma}

Example
-------

Consider the previous example where a population with three different agent
types is playing the prisoner's dilemma game.  Transforming that evolutionary
game into an `evolutionary game with pseudo-pure strategies` results in the
following pseudo-pure strategy payout matrix :math:`\boldsymbol{A}^*`:

.. math::

   \boldsymbol{A}^* &= \boldsymbol{X}^T\boldsymbol{A}\boldsymbol{X} \\
   &=
   \begin{pmatrix}0.25 & 0.75 \\ 0.5 & 0.5 \\ 0.75 & 0.25\end{pmatrix}
   \begin{pmatrix}3 & 0 \\ 5 & 1\end{pmatrix}
   \begin{pmatrix}0.25 & 0.5 & 0.75 \\ 0.75 & 0.5 & 0.25\end{pmatrix} \\
   &=
   \begin{pmatrix}1.6875 & 2.6250 & 3.5625 \\
                  1.3750 & 2.2500 & 3.1250  \\
                  1.0625 & 1.8750 & 2.6875\end{pmatrix}

The expected payouts for the three mixed-strategy types are the following:

.. math::

   u_1 =& \boldsymbol{e}_1^*\boldsymbol{A}^*\boldsymbol{\sigma} \\
   =&
   \begin{pmatrix}1 & 0 & 0\end{pmatrix}
   \begin{pmatrix}1.6875 & 2.6250 & 3.5625 \\
                  1.3750 & 2.2500 & 3.1250  \\
                  1.0625 & 1.8750 & 2.6875\end{pmatrix}
   \begin{pmatrix}0.2 \\ 0.5 \\ 0.3\end{pmatrix} \\
   =&
   2.71875

   u_2 =& \boldsymbol{e}_2^*\boldsymbol{A}^*\boldsymbol{\sigma} \\
   =&
   \begin{pmatrix}0 & 1 & 0\end{pmatrix}
   \begin{pmatrix}1.6875 & 2.6250 & 3.5625 \\
                  1.3750 & 2.2500 & 3.1250  \\
                  1.0625 & 1.8750 & 2.6875\end{pmatrix}
   \begin{pmatrix}0.2 \\ 0.5 \\ 0.3\end{pmatrix} \\
   =&
   2.3375

   u_3 =& \boldsymbol{e}_3^*\boldsymbol{A}^*\boldsymbol{\sigma} \\
   =&
   \begin{pmatrix}0 & 0 & 1\end{pmatrix}
   \begin{pmatrix}1.6875 & 2.6250 & 3.5625 \\
                  1.3750 & 2.2500 & 3.1250  \\
                  1.0625 & 1.8750 & 2.6875\end{pmatrix}
   \begin{pmatrix}0.2 \\ 0.5 \\ 0.3\end{pmatrix} \\
   =&
   1.95625

The population average payout is equal to the following:

.. math::

   \bar{u}_{\boldsymbol{\sigma}}=&
   \mathop{\mathbb{E}}\limits_{\boldsymbol{a} \in \mathcal{A}}
   [\mathit{u}_a \mid \boldsymbol{\sigma}]=
   \boldsymbol{\sigma}\boldsymbol{A}^*\boldsymbol{\sigma} \\
   =&
   \begin{pmatrix}0.2 & 0.5 & 0.3\end{pmatrix}
   \begin{pmatrix}1.6875 & 2.6250 & 3.5625 \\
                  1.3750 & 2.2500 & 3.1250  \\
                  1.0625 & 1.8750 & 2.6875\end{pmatrix}
   \begin{pmatrix}0.2 \\ 0.5 \\ 0.3\end{pmatrix} \\
   =&
   2.299375

As expected, these results are identical to the results produced in the
previous example.

------------------------------
Transformed Evolutionary Games
------------------------------

Let :math:`\mathcal{G}` be a symmetric two-player game with :math:`\mathit{m}`
pure strategies that is the `stage game` for an evolutionary game played by a
population of agents playing :math:`\mathit{n}` different mixed strategies.

The game can be transformed into an asymmetric game :math:`\mathcal{G}^*`
where the strategies played by position one are the :math:`\mathit{m}` pure
strategies defined by the original game :math:`\mathcal{G}` and the strategies
played by position two are the :math:`\mathit{n}` mixed strategies played by
the agents in the population.

Let :math:`\boldsymbol{A}^*` be the payout matrix for the transformed game
:math:`\mathcal{G}^*`. The entry in row :math:`\mathit{h}` and column
:math:`\mathit{k}` in matrix :math:`\boldsymbol{A}^*` is the expected payout
for an agent in position one playing pure strategy :math:`\boldsymbol{e}_h`
against an opponent in position two playing mixed strategy
:math:`\boldsymbol{x}_{k}`.

.. math::

   \mathit{a}^*_{h,k} =
   \mathop{\mathbb{E}}[\mathit{u}(\boldsymbol{\chi})
   \mid
   \boldsymbol{\chi}=(\boldsymbol{e}_h, \boldsymbol{x}_k)] =
   \sum_{j=0}^m a_{h,j} \cdot x_{k,j}

Given the payout matrix :math:`\boldsymbol{A}` for the original game and the
population mixed-strategy profile matrix :math:`\boldsymbol{X}`, the payout
matrix :math:`\boldsymbol{A}^*` for the transformed game is the following:

.. math::

   \boldsymbol{A}^*=\boldsymbol{A}\boldsymbol{X}

In the context of the transformed game :math:`\mathcal{G}^*`, the population
state vector :math:`\boldsymbol{\sigma}`, defines the population mixed-strategy
for position two.

Given payout matrix :math:`\boldsymbol{A}^*`, the expected payout for an agent
playing mixed strategy :math:`\boldsymbol{x}_i` against an agent that is
randomly selected from a population in state :math:`\boldsymbol{\sigma}` is
equivalent to the expected payout for the same agent playing against an agent
that is using population mixed-strategy
:math:`\boldsymbol{x}_{\boldsymbol{\sigma}}`.

.. math::

   u_{\boldsymbol{x}_k} =
   \boldsymbol{x}_k\boldsymbol{A}\boldsymbol{x}_{\boldsymbol{\sigma}}

Replacing the vector :math:`\boldsymbol{x}_k` with the population
mixed-strategy profile matrix :math:`\boldsymbol{X}` in the previous equation
provides a matrix equation that generates the vector :math:`\boldsymbol{u}` of
expected payouts for all mixed strategy types:

.. math::

   \boldsymbol{u} = (u_1, u_2, \dots, u_n) = 
   \boldsymbol{X}\boldsymbol{A}^*\boldsymbol{\sigma}

The `population average payout` is the expected payout earned by
one randomly selected agent playing against a second randomly selected agent.
Since two agents selected randomly from the population to play a game can
equivelently be treated as two agents that are both playing the population
mixed-strategy :math:`\boldsymbol{\sigma}`, the population average payout is
equal to the mixed-strategy payout when mixed strategy profile
:math:`(\boldsymbol{\sigma},\boldsymbol{\sigma})` is in effect.

.. math::

   \bar{u}_{\boldsymbol{\sigma}}=
   \mathop{\mathbb{E}}\limits_{\boldsymbol{a} \in \mathcal{A}}
   [\mathit{u}_a \mid \boldsymbol{\sigma}]=
   \boldsymbol{\sigma}\boldsymbol{A}^*\boldsymbol{\sigma}

---------------------
Evolutionary Dynamics
---------------------
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


The ``egt`` package currently supports the use of `2-person symmetric` games
as the `stage game` for evolutionary games.