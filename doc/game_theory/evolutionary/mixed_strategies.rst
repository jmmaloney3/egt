.. title:: Games with Mixed Strategies

.. _evolutionary_mixed_strategies:

Evolutionary Games with Mixed Strategies
========================================

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