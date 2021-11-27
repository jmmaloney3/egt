.. title:: Games with Mixed Strategies

.. _normal_form_mixed_strategies:

Normal Form Games with Mixed Strategies
=======================================

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

The `combined mixed-strategy payoff function`
:math:`\boldsymbol{u}(\boldsymbol{\chi})=
(u_1(\boldsymbol{\chi}),u_2(\boldsymbol{\chi}),
\dots,u_n(\boldsymbol{\chi})`
provides a vector representing the payoffs for each player position for
mixed-strategy profile :math:`\boldsymbol{\chi}`.

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


