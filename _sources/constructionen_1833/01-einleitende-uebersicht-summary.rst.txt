:title: Steiner (1833) §§ 1–2 — Summary & Comparative Regimes
:track_label: Summary
:layout: book
:order: 1
:folio: 0007
:tracks: English: 01-einleitende-uebersicht-en | Deutsch (1833): 01-einleitende-uebersicht-de | Summary: 01-einleitende-uebersicht-summary | Notes: 01-einleitende-uebersicht-notes

.. _steiner-01-summary:

========================================================================================
Summary: The Minimal-Instrument Regimes & Algebraic Constructibility
========================================================================================

.. rubric:: Comparative Architecture of Ruler+Compass, Mascheroni Compass-Only, and Poncelet–Steiner Fixed-Circle

1. Instrument Regimes & Operation Subspaces
-------------------------------------------

.. list-table:: Constructibility & Operation Subspaces Across Classical and Minimal Instruments
   :header-rows: 1
   :widths: 24 24 26 26

   * - Regime
     - Primary Literature
     - Operation Symbol
     - Algebraic Field & Invariance
   * - **Canonical Ruler + Compass**
     - :person:`Euclid <euclid>` (:cite:`euclid-elements`), :person:`Lemoine <lemoine>` (:cite:`lemoine-1902`)
     - :math:`l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3`
     - Full Euclidean quadratic closure :math:`\mathbb{E}` (nested square roots :math:`\sqrt{x^2 \pm y^2}`)
   * - **Mascheroni Compass Alone**
     - :person:`Mohr <mohr>` (:cite:`mohr-1672`), :person:`Mascheroni <mascheroni>` (:cite:`mascheroni-1797`)
     - :math:`m_1 C_1 + m_2 C_2 + m_3 C_3` (:math:`l_1 = l_2 = 0`)
     - Full Euclidean quadratic closure :math:`\mathbb{E}` (straight lines implicit as point-pairs :math:`(A, B)`)
   * - **Poncelet–Steiner Straightedge + Fixed Circle :math:`M`**
     - :person:`Poncelet <poncelet>` (:cite:`poncelet-1822`), :person:`Steiner <steiner>` (:cite:`steiner-1833`)
     - :math:`l_1 R_1 + l_2 R_2` (:math:`m_1 = m_2 = m_3 = 0`)
     - Full Euclidean quadratic closure :math:`\mathbb{E}` (circles implicit as center :math:`M_1` + radius endpoint)
   * - **Hilbert Straightedge + Eichmaß (Unit Gauge)**
     - :person:`Hilbert <hilbert>` (:cite:`hilbert-1899`, §§ 36–39)
     - :math:`R_1, R_2` + movable unit-segment transferrer
     - Strictly *Pythagorean* subfield :math:`\Omega_{\text{pyth}}` (:math:`\sqrt{1 + \omega^2}`, strictly smaller than :math:`\mathbb{E}`)

2. The Eight Fundamental Problems (*Drittes Kapitel*, § 18)
------------------------------------------------------------

.. list-table:: Steiner's Eight Fundamental Tasks
   :header-rows: 1
   :widths: 12 40 24 24

   * - Task
     - Problem Statement
     - Primary Apparatus
     - Operation Count
   * - **Erste**
     - Parallel through a point to a given line (``[68]``–``[71]``)
     - Complete quadrangle on diameter :math:`ab`
     - :math:`11R_1 + 6R_2, S = 17`
   * - **Zweite**
     - Segment multiplication and rational division (``[71]``)
     - Parallel lines + harmonic diagonals
     - Pure linear scaling
   * - **Dritte**
     - Perpendicular to a given line through a point (``[71]``–``[75]``)
     - Thales chord / orthocenter on diameter
     - :math:`10R_1 + 5R_2, S = 15`
   * - **Vierte**
     - Angle copy to a given vertex and ray (``[75]``)
     - Parallel chords in fixed circle :math:`\Omega`
     - Pure straightedge transport
   * - **Fünfte**
     - Angle bisection and multiplication (``[75]``–``[76]``)
     - Subtended chord parallel in :math:`\Omega`
     - Straightedge bisection
   * - **Sechste**
     - Segment transfer from a point along a ray (``[76]``–``[78]``)
     - Centers of similitude :term:`A, I <aehnlichkeitspunkte>`
     - Homothetic ray projection
   * - **Siebente**
     - Line intersection with virtual circle :math:`(M_1, r_1)` (``[78]``–``[82]``)
     - Homothetic projection to drawn circle :math:`\Omega`
     - Line–line transfer
   * - **Achte**
     - Intersection of two virtual circles (``[82]``–``[85]``)
     - :term:`Radical axis <linie-der-gleichen-potenzen>` reduced to Task 7
     - Complete Euclidean reduction
