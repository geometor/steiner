:layout: book
:canonical_id: Prob. 3
:breadcrumb_title: Prob. 3
:order: 4
:folio: 0056
:track_label: English
:tracks: English: index | German: de | Summary: summary | Notes: notes
:title: Third Problem (§ 18, [71]–[75]): Dropping a Perpendicular to a Straight Line

.. _steiner-en-aufgabe-3:

.. folio:: 0056
   :page: 52

Third Problem (§ 18, [71]–[75]): Dropping a Perpendicular to a Straight Line
============================================================================

.. rubric:: Jakob Steiner — *Die geometrischen Constructionen* (Berlin, 1833 / Leipzig, 1895)

« *Through any given point, to draw a straight line perpendicular to a given straight line.* »

.. picture:: 0057.g1.svg
   :alt: Figure 20 — Dropping a perpendicular to line pq using Thales semicircle chords on diameter ab of fixed circle M (§ 18, Problem 3)
   :caption: Fig. 20 — Fixed circle M, diameter ab, chords ac, ad, bc, and perpendicular ar onto given line pq (§ 18, Problem 3)

.. collapse:: Archival Plate — Folio 0057, Fig. 20 (1895, p. 53)

   .. picture:: 0057.g1.png
      :alt: Archival scan of Fig. 20 from Ostwald's Klassiker Nr. 60 (p. 53)

**Solution A (Via** :term:`Thales' Theorem <satz-des-thales>`):
  Draw diameter :g:`ab <0057.g1:/ a b />` of fixed circle :g:`M <0057.g1:M>` parallel to the given line :g:`pq <0057.g1:/ p q />` (or take :g:`ab <0057.g1:/ a b />` perpendicular to :g:`pq <0057.g1:/ p q />` as in Fig. 20 via a chord pair :g:`ad <0057.g1:/ a d />` and :g:`bd <0057.g1:/ b d />`). For any point :g:`c <0057.g1:c>` on the circumference of :math:`\Omega`, Thales' theorem guarantees :math:`\angle acb = 90^\circ`. Drawing through the given point a line parallel to the right-angle leg (by Problem 1) yields the required perpendicular.

**Solution B (Via the** :term:`Orthocenter <orthocentrum>` **of a Triangle on Diameter** :math:`ab`):
  Choose vertex :math:`S` off diameter :g:`ab <0057.g1:/ a b />`. Rays :math:`Sa, Sb` cut :math:`\Omega` at :math:`c, d`. Because :math:`\angle acb = \angle adb = 90^\circ`, chords :math:`ad` and :math:`bc` are the exact altitudes of :math:`\triangle abS`. Their intersection :math:`H` is the orthocenter, so line :math:`SH` is strictly perpendicular to :math:`ab` in just **5 straight lines**:

  .. math::

     \mathrm{Op.}_{\text{Perpendicular}} : 10R_1 + 5R_2, \qquad S = 15, \quad E = 10, \quad N_{\text{circles}} = 0.

.. toctree::
   :hidden:

   de
   summary
   notes
