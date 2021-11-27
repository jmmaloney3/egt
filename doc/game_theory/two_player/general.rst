.. title:: General Games

.. _two_player_general:

General 2-Player Normal Form Games
==================================

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

