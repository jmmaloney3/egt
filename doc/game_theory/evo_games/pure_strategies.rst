.. title:: Games with Pure Strategies

.. _evolutionary_pure_strategies:

Evolutionary Games with Pure Strategies
=======================================

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