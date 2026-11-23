:layout: book
:canonical_id: § 7
:breadcrumb_title: § 7
:order: 5
:folio: 0019
:track_label: English
:tracks: English: index | German: de | Summary: summary | Notes: notes
:title: § 7: Parallels from Rational Segment Ratios

.. folio:: 0019
   :page: 15

§ 7: Parallels from Rational Segment Ratios
===========================================

.. rubric:: Jakob Steiner — *Die geometrischen Constructionen* (Berlin, 1833 / Leipzig, 1895)

.. picture:: 0019.g2.svg
   :alt: Figure 6 — Parallels from two adjacent segments BD, DC in rational ratio (§ 7)
   :caption: Fig. 6 — Adjacent segments BD and DC in given rational ratio a : b (§ 7)

.. collapse:: Archival Plate — Folio 0019, Fig. 6 (1895, p. 15)

   .. picture:: 0019.g2.png
      :alt: Archival scan of Fig. 6 from Ostwald's Klassiker Nr. 60 (p. 15)

*Problem (§ 7)*: *Given two adjacent collinear segments* :g:`BD <0019.g2:/ B D />` *and* :g:`DC <0019.g2:/ D C />` *having any given rational ratio* :math:`a : b`, *to draw a line parallel to* :g:`BC <0019.g2:/ B E />` *through any given point using the straightedge alone.*

Let :math:`a > b` be coprime integers. Constructing the fourth harmonic point :g:`E <0019.g2:E>` conjugate to :g:`C <0019.g2:C>` with respect to :g:`B <0019.g2:B>` and :g:`D <0019.g2:D>` (§ 5, I) produces segment :math:`CE = x` satisfying :math:`a : b = (a + b + x) : x`, whence :math:`x = \frac{b(a+b)}{a-b}`, and therefore:

.. math::

   BC : CE = a - b : b \quad (\text{or } a : z = a - b : 2b \text{ with } z = DE).

Iterating this Euclidean subtraction step (:math:`a, b \to a-b, b \to \dots`) strictly decreases the integer terms until two equal adjacent segments in the ratio :math:`1 : 1` are obtained—reducing the construction immediately to **§ 6, I**!

.. toctree::
   :hidden:

   de
   summary
   notes
