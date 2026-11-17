:title: Steiner (1833) §§ 1–2 — Notes & Critical Commentary
:track_label: Notes
:layout: book
:order: 1
:folio: 0007
:tracks: English: 01-einleitende-uebersicht-en | German: 01-einleitende-uebersicht-de | Summary: 01-einleitende-uebersicht-summary | Notes: 01-einleitende-uebersicht-notes

.. _steiner-01-notes:

========================================================================================
Notes & Commentary: Projective Obstructions & The Poncelet–Steiner Theorem
========================================================================================

.. rubric:: Epistemological Foundations of Minimal Instruments & Field Closures

1. Why a Straightedge Alone in an Empty Plane Fails
---------------------------------------------------

A common misconception in elementary geometry is that a straightedge alone can draw parallels or bisect segments. Projective geometry demonstrates why this is mathematically impossible:

* Any projective collineation maps straight lines to straight lines and preserves incidence and cross-ratios.
* However, general collineations do **not** preserve distance, parallelism, or right angles: they can map the line at infinity :math:`\ell_\infty` to an arbitrary ordinary line, and they transform circles into arbitrary conics.
* Consequently, in a completely empty plane without any fixed metric or affine locus, the straightedge can construct only projectively invariant objects (such as harmonic conjugates from complete quadrangles, or the fourth harmonic ray). It cannot construct midpoints, cannot draw parallels, and cannot extract square roots.

2. Why One Circle with Center :math:`M` Restores the Full Metric
-----------------------------------------------------------------

Once a single circle :term:`Omega <fester-huelfskreis>` together with its center :math:`M` is permanently drawn in the plane, the projective group is dramatically restricted:

* The center :math:`M` bisects every diameter :math:`ab` passing through it. Therefore, along any diameter line, the harmonic conjugate of :math:`M` with respect to :math:`a, b` is the point at infinity :math:`\infty` on that line!
* By the harmonic properties of the complete quadrangle (§ 6 and Erste Aufgabe), this single bisected segment allows the straightedge to construct the parallel to :math:`ab` through *any* point in the plane.
* Furthermore, by Thales' theorem (§ 18, Dritte Aufgabe), any angle inscribed in a semicircle of :math:`\Omega` is a right angle :math:`90^\circ`. This supplies an intrinsic orthogonal involution.
* Finally, the continuous drawn circumference of :math:`\Omega` serves as a permanent quadratic oracle: any quadratic equation :math:`x^2 - 2px + q = 0` can be mapped homothethically to the intersection of a secant line with :math:`\Omega` (Siebente Aufgabe)!

3. The Indispensability of the Center :math:`M`
-----------------------------------------------

If the circle :math:`\Omega` were given **without** its center :math:`M`, can :math:`M` be found by straightedge alone?

The answer is rigorously **no**. The group of projective collineations that leave a circle :math:`\Omega` invariant is isomorphic to the group of hyperbolic motions of the Klein/Poincaré disk model. Any such collineation maps :math:`\Omega` onto itself and straight lines onto straight lines, yet moves the Euclidean center :math:`M` to another interior point :math:`M' \ne M`. Because every straightedge construction is invariant under projective collineations that preserve the given configuration, no straightedge construction from :math:`\Omega` alone can distinguish the true Euclidean center :math:`M` from any other interior point!

Thus, the presence of the center :math:`M` is mathematically essential to the Poncelet–Steiner theorem.
