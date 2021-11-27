.. title:: Notation

.. _notation:

Notation
========

The following table provides a reference to the notation used
in this game theory overview.

.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - .. centered:: Variable
     - .. centered:: Type
     - Description
   * - .. centered:: :math:`\mathcal{G}`
     - .. centered:: Tuple
     - A `normal form game`.
   * - .. centered:: :math:`\mathcal{I}`
     - .. centered:: Set
     - The set of `player positions` for the game.
   * - .. centered:: :math:`\mathit{n}`
     - .. centered:: Scalar
     - The number of player positions in the game
       (i.e. the size of set :math:`\mathcal{I}`).
   * - .. centered:: :math:`\mathcal{S}_i`
     - .. centered:: Set
     - The set of `pure strategies` for player :math:`\mathit{i}`.
   * - .. centered:: :math:`\mathit{m_i}`
     - .. centered:: Scalar
     - The number of pure strategies for player position
       :math:`\mathit{i}` (i.e. the size of set :math:`\mathcal{S}_i`).
   * - .. centered:: :math:`s_i`
     - .. centered:: Scalar
     - The `pure strategy` assigned to player position :math:`\mathit{i}`.
   * - .. centered:: :math:`\mathcal{S}`
     - .. centered:: Set
     - The `pure-strategy space` of the game.
   * - .. centered:: :math:`\boldsymbol{s}`
     - .. centered:: Vector
     - A `pure-strategy profile` from the game's `pure-strategy space`.
   * - .. centered:: :math:`\pi_i(\boldsymbol{s})`
     - .. centered:: Scalar Function
     - The `pure-strategy payoff function` for position :math:`\mathit{i}`.
   * - .. centered:: :math:`\boldsymbol{\pi}(\boldsymbol{s})`
     - .. centered:: Vector Function
     - The `combined pure-strategy payoff function` for the game.
   * - .. centered:: :math:`\boldsymbol{x}_i`
     - .. centered:: Vector
     - The `mixed strategy` for player positon :math:`\mathit{i}`.
   * - .. centered:: :math:`\boldsymbol{e}_{i,h}`
     - .. centered:: Vector
     - The `mixed strategy` for player positon :math:`\mathit{i}` that always
       plays `pure strategy` :math:`\mathit{h} \in \mathcal{S}_i`.
   * - .. centered:: :math:`x_{i,h}`
     - .. centered:: Scalar
     - The component of `mixed strategy` :math:`\boldsymbol{x}_i`
       that specifies the probability that pure strategy
       :math:`\mathit{h}` will be used.
   * - .. centered:: :math:`\boldsymbol{\chi}`
     - .. centered:: Tuple of Vectors
     - A `mixed strategy profile` for the game.
   * - .. centered:: :math:`u_i(\boldsymbol{\chi})`
     - .. centered:: Scalar Function
     - The `mixed-strategy payoff function` for player position
       :math:`\mathit{i}`.
   * - .. centered:: :math:`\boldsymbol{u}(\boldsymbol{\chi})`
     - .. centered:: Vector Function
     - The `combined mixed-strategy payoff function` for the game.
   * - .. centered:: :math:`\boldsymbol{A}`
     - .. centered:: Matrix
     - The `payoff matrix` for player position one in a two player normal
       form game.
   * - .. centered:: :math:`a_{h,k}`
     - .. centered:: Scalar
     - The payoff specified by `payoff matrix` :math:`\boldsymbol{A}`
       when player position one uses pure strategy :math:`\mathit{h}`
       and player position two uses pure strategy :math:`\mathit{k}`
   * - .. centered:: :math:`\boldsymbol{B}`
     - .. centered:: Matrix
     - The `payoff matrix` for player position two in a two player normal
       form game.
   * - .. centered:: :math:`b_{h,k}`
     - .. centered:: Scalar
     - The payoff specified by `payoff matrix` :math:`\boldsymbol{B}`
       when player position one uses pure strategy :math:`\mathit{h}`
       and player position two uses pure strategy :math:`\mathit{k}`