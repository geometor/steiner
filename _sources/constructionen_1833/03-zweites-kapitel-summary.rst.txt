:title: Steiner (1833) §§ 11–17 — Summary of Chapter II
:track_label: Summary
:layout: book
:order: 3
:folio: 0032
:tracks: English: 03-zweites-kapitel-en | German: 03-zweites-kapitel-de | Summary: 03-zweites-kapitel-summary | Notes: 03-zweites-kapitel-notes

.. _steiner-03-summary:

========================================================================================================================
Summary: Similitude Pencils, Radical Axes & Power Centers
========================================================================================================================

.. rubric:: Homothetic Ratios, Radical Line Formulas & Operation Costs

1. Centers of Similitude Formula
--------------------------------

For two circles centered at :math:`M = (x_M, y_M)` and :math:`M_1 = (x_{M_1}, y_{M_1})` with radii :math:`R, r_1`:

.. math::

   A = \frac{R\,M_1 - r_1\,M}{R - r_1}, \qquad I = \frac{R\,M_1 + r_1\,M}{R + r_1}.

Both points lie on the line of centers :math:`MM_1` and form a harmonic range with the centers: :math:`(M, M_1; A, I) = -1`.

2. Radical Axis Equation & Orthogonality
----------------------------------------

In Cartesian coordinates with centers at :math:`(0, 0)` and :math:`(d, 0)`:

.. math::

   x^2 + y^2 - R^2 = (x - d)^2 + y^2 - r_1^2 \iff 2dx = d^2 + R^2 - r_1^2.

This yields a vertical line perpendicular to the line of centers at distance :math:`x = \frac{d^2 + R^2 - r_1^2}{2d}` from :math:`M`.

.. list-table:: Similitude & Radical Axis Primitives in Chapter II
   :header-rows: 1
   :widths: 26 34 20 20

   * - Primitive
     - Construction Method
     - Operation Symbol
     - Simplicity (:math:`S, E`)
   * - **Centers of Similitude :math:`(A, I)`**
     - Parallel radii join + center line (§ 12)
     - :math:`8R_1 + 4R_2`
     - :math:`S = 12, E = 8`
   * - **Four Axes of Similitude**
     - Three pairwise center joins (§ 13)
     - Straightedge join
     - Pure collineation
   * - **Radical Axis (Two Circles)**
     - Auxiliary secants + perpendicular join (§ 17)
     - :math:`11R_1 + 6R_2`
     - :math:`S = 17, E = 11`
   * - **Radical Center (Three Circles)**
     - Intersection of two radical axes
     - Straightedge meet
     - Pure incidence
