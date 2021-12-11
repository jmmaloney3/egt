.. title:: Symmetric Games

.. _two_player_symmetric:

Symmetric 2-Player Normal Form Games
====================================

In the special case of a `symmetric`
:ref:`two-player normal form game <two_player_general>`, each player
position has :math:`m` pure strategies and the pair of :math:`m \times m`
payoff matrices :math:`(\boldsymbol{A},\boldsymbol{B})` meets the following
aditional requirement:

.. math::

   \boldsymbol{B} = \boldsymbol{A}^T

This implies that the payoff accrued by a pure strategy is independent of the
player position that plays that strategy.   Therefore, for all
:math:`h,k \in \mathcal{S}=\mathcal{S}_1=\mathcal{S}_2`, given two
:ref:`pure strategy profiles <pure_strategy_profile>`
:math:`\boldsymbol{s}_{h,k}=(h,k)` and
:math:`\boldsymbol{s}_{k,h}=(k,h)` that are identical except that the pure
strategies assigned to each player position have been swapped, the
:ref:`pure-strategy payoff functions <pure_strategy_payoff_function>`
for the two player positions satisfy the following conditions:

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

Using the :ref:`mixed strategy representation for pure strategies 
<mixed_strategy_rep_for_pure_strategy>`,
the :ref:`mixed strategy profile <mixed_strategy_profile>`...

TBD

Using the definitions given above for the two pure strategy payoff functions
for a symmetric two player game, the two
:ref:`mixed strategy payoff functions <mixed_strategy_payoff_function>`
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

