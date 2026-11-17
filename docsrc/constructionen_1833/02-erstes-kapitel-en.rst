:title: Steiner (1833) §§ 3–10 — Chapter I: Harmonic Ranges, Complete Quadrangle & Polars (English)
:track_label: English
:layout: book
:order: 2
:folio: 0010
:tracks: English: 02-erstes-kapitel-en | German: 02-erstes-kapitel-de | Summary: 02-erstes-kapitel-summary | Notes: 02-erstes-kapitel-notes

.. _steiner-02-en:

=================================================================================================================
Chapter I: Harmonic Rays and Points, Complete Quadrangle and Polars (§§ 3–10)
=================================================================================================================

.. rubric:: Jakob Steiner — *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises* (Berlin, 1833, pp. 7–28 / ``[7]``–``[28]``)

.. contents:: In This Chapter
   :local:
   :depth: 2
   :backlinks: none

.. _steiner-en-s03:

.. folio:: 0010
   :page: 7

§§ 3–5. Harmonic Rays and Harmonic Point Ranges
-----------------------------------------------

Four concurrent straight lines :math:`a, b, c, d` emanating from a common vertex :math:`S` form a :term:`harmonic pencil of rays <harmonische-strahlen>` if every transversal intersecting them in four points :math:`A, B, C, D` produces a :term:`harmonic range <harmonische-punkte>`, defined by the invariant cross-ratio:

.. math::

   (A, B; C, D) = \frac{AC}{BC} : \frac{AD}{BD} = -1.

Under this condition, points :math:`C` and :math:`D` harmonically separate the pair :math:`A, B`. In particular, if :math:`D` recedes to infinity along the carrier line (:math:`AD/BD \to 1`), then :math:`AC/BC = -1`, meaning that :math:`C` is the exact **midpoint** of segment :math:`AB`!

.. _steiner-en-s06:

.. folio:: 0015
   :page: 14

§ 6. The Complete Quadrangle and Complete Quadrilateral
-------------------------------------------------------

Four coplanar points, no three collinear, constitute a :term:`complete quadrangle <vollstaendiges-viereck>`. They determine six connecting lines (sides) meeting pairwise in three **diagonal points**.

Dually, four coplanar straight lines, no three concurrent, constitute a :term:`complete quadrilateral <vollstaendiges-vierseit>`.

*Theorem*: On every diagonal of a complete quadrangle, the two opposite sides and the remaining two diagonal points harmonically separate each other.

This yields the fundamental straightedge construction:

*Given three collinear points :math:`A, B, C`, to construct the fourth harmonic conjugate :math:`D` using only a straightedge.*

1. Choose an arbitrary vertex :math:`S` off the line :math:`AB`.
2. Draw rays :math:`SA, SB, SC`.
3. Draw an arbitrary transversal through :math:`A` meeting :math:`SC` at :math:`P` and :math:`SB` at :math:`Q`.
4. Join :math:`BP` and :math:`SQ` meeting at :math:`R`.
5. Join :math:`AR`: its intersection with line :math:`AB` is the required fourth harmonic point :math:`D`!

.. _steiner-en-s07:

.. folio:: 0020
   :page: 20

§§ 7–10. Polar Lines and Poles with Respect to a Circle
-------------------------------------------------------

If any secant drawn through a pole :math:`P` cuts a given circle in points :math:`A` and :math:`B`, and on this secant the fourth harmonic point :math:`Q` is determined such that :math:`(A, B; P, Q) = -1`, the locus of all such conjugate points :math:`Q` as the secant rotates is a single straight line: the :term:`polar <pol-und-polare>` :math:`p` of :math:`P` with respect to the circle.

Because the polar relation is purely harmonic, the straightedge alone constructs it for any point :math:`P`:

1. Draw two secants through :math:`P` cutting the circle at :math:`A, B` and :math:`C, D`.
2. Join the cross-chords: :math:`AD \cap BC = E` and :math:`AC \cap BD = F`.
3. Line :math:`EF` is the polar line :math:`p` of :math:`P`!

If :math:`P` lies outside the circle, polar :math:`p` cuts the circumference in the exact points of contact of the two tangents from :math:`P`—allowing tangents to any drawn circle to be constructed with a straightedge alone in :math:`16R_1 + 9R_2` (:math:`S = 25`, zero circles)!

.. picture:: /_static/figures/pappus_steiner.svg
