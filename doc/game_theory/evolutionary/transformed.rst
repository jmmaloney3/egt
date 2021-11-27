.. title:: Transformed Games

.. _evolutionary_transformed:

Transformed Evolutionary Games
==============================

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