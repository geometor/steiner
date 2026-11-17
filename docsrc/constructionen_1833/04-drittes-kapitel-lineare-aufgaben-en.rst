:title: Steiner (1833) § 18 (Problems 1–5) — Linear & Angular Straightedge Constructions (English)
:track_label: English
:layout: book
:order: 4
:folio: 0054
:tracks: English: 04-drittes-kapitel-lineare-aufgaben-en | German: 04-drittes-kapitel-lineare-aufgaben-de | Summary: 04-drittes-kapitel-lineare-aufgaben-summary | Notes: 04-drittes-kapitel-lineare-aufgaben-notes

.. _steiner-04-en:

========================================================================================================================
Chapter III: The First Five Fundamental Problems — Linear & Angular Constructions (§ 18, [68]–[76])
========================================================================================================================

.. rubric:: Jakob Steiner — *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises* (Berlin, 1833, pp. 50–56 / ``[68]``–``[76]``)

.. contents:: Problems in This Section
   :local:
   :depth: 2
   :backlinks: none

.. _steiner-en-aufgabe-1:

.. folio:: 0054
   :page: 50

First Problem (``[68]``–``[71]``): Drawing a Parallel Through Any Given Point
-----------------------------------------------------------------------------

« *Through any given point, to draw a straight line parallel to any given straight line.* »

**Case a: When the given line passes through the center :math:`M` of the fixed circle.**
  The given line cuts the fixed circle :math:`\Omega` in a diameter :math:`ab` bisected at :math:`M`. Let :math:`P` be the given external point.
  1. Choose an arbitrary vertex :math:`S` off the diameter line.
  2. Draw the three reference rays :math:`Sa, SM, Sb`.
  3. Through :math:`P`, draw any transversal line meeting these rays in :math:`a', M', b'`.
  4. Cross-join the points: draw :math:`ab'` and :math:`ba'` meeting at :math:`O`.
  5. Ray :math:`SO` meets the transversal at the harmonic center :math:`K`.
  6. The complete quadrangle diagonals produce the exact parallel :math:`PQ \parallel ab` in **6 straight lines**:

  .. math::

     \mathrm{Op.}_{\text{Parallel}} : 11R_1 + 6R_2, \qquad S = 17, \quad E = 11, \quad N_{\text{circles}} = 0.

**Case b: When the given line does not pass through :math:`M`.**
  Draw two secants through :math:`M` parallel to the line, or transfer the line to a parallel diameter through :math:`M`, reducing the construction to Case a.

.. _steiner-en-aufgabe-2:

.. folio:: 0056
   :page: 52

Second Problem (``[71]``): Segment Multiplication and Rational Division
------------------------------------------------------------------------

« *Given a bounded segment on a straight line:*
  *a) To find another segment that is any given integer multiple of the first;*
  *b) To divide the given segment into any given number of equal parts;*
  *c) To construct a segment having any given rational ratio to the first.* »

By Problem 1, draw a parallel line at arbitrary distance. Stepping equal segments along the parallel and projecting rays through a perspective center divides or multiplies the original segment by pure straightedge incidence (Euclid VI.9–10).

.. _steiner-en-aufgabe-3:

.. folio:: 0056
   :page: 52

Third Problem (``[71]``–``[75]``): Dropping a Perpendicular to a Straight Line
------------------------------------------------------------------------------

« *Through any given point, to draw a straight line perpendicular to a given straight line.* »

**Solution A (Via Thales' Theorem):**
  Draw diameter :math:`ab` of :math:`\Omega` parallel to the given line. For any point :math:`c` on the circumference of :math:`\Omega`, :term:`Thales' theorem <satz-des-thales>` guarantees that :math:`\angle acb = 90^\circ`. Drawing a line through the given point parallel to :math:`bc` (by Problem 1) yields the required perpendicular.

**Solution B (Via the Orthocenter of a Triangle on Diameter :math:`ab`):**
  Choose vertex :math:`S` off diameter :math:`ab`. Rays :math:`Sa, Sb` cut :math:`\Omega` at :math:`c, d`. Since :math:`\angle acb = \angle adb = 90^\circ`, chords :math:`ad` and :math:`bc` are the exact altitudes of :math:`\triangle abS`. Their intersection :math:`H` is the :term:`orthocenter <orthocentrum>`. Line :math:`SH` is therefore perpendicular to diameter :math:`ab` in just **5 straight lines**:

  .. math::

     \mathrm{Op.}_{\text{Perpendicular}} : 10R_1 + 5R_2, \qquad S = 15, \quad E = 10, \quad N_{\text{circles}} = 0.

.. _steiner-en-aufgabe-4-5:

.. folio:: 0059
   :page: 55

Fourth & Fifth Problems (``[75]``–``[76]``): Laying Off and Bisecting Angles
-----------------------------------------------------------------------------

« *Fourth Problem: Through a given point, to draw a straight line making with a given straight line an angle equal to a given angle.* »

« *Fifth Problem: To bisect a given angle, or to multiply it by any integer.* »

Draw diameters :math:`ab, cd` of the fixed circle :math:`\Omega` parallel to the arms of the given angle, transporting the angle directly to center :math:`M` as central angle :math:`\angle aMc`.

To **bisect** the angle (Problem 5), draw chord :math:`ad`. In isosceles :math:`\triangle aMd`, the altitude from :math:`M` perpendicular to chord :math:`ad` bisects :math:`\angle aMc`. By Problem 1, drawing a parallel to chord :math:`ad` through :math:`M` immediately bisects the angle using only the straightedge!

.. picture:: /_static/figures/pappus_parallel_steiner.svg
