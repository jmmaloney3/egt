.. title:: Games with Pseudo-pure Strategies

.. _evo_games_pseudo_pure_strategies:

Evolutionary Games with Pseudo-pure Strategies
==============================================

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