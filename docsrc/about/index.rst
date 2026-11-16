:navigation: header
:order: 10

=====
About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

The mission of this repository is to establish the definitive Digital Scriptorium edition of :person:`Jakob Steiner <steiner>`'s seminal 1833 treatise, *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises*, paired with exact symbolic geometry in :mod:`geometor.steiner`.

Euclidean geometry traditionally postulates *both* the ungraduated straightedge (Postulates 1–2) and the compass (Postulate 3). Between 1672 and 1890, synthetic and projective geometers discovered that either instrument can dispense with the other—provided a subtle asymmetry between circles and lines is respected:

1. **Compass Alone — Georg Mohr (1672) & Lorenzo Mascheroni (1797)**:
   First proved by :person:`Georg Mohr <mohr>` in *Euclides Danicus* (:cite:`mohr-1672`) and independently developed by :person:`Lorenzo Mascheroni <mascheroni>` in *La Geometria del Compasso* (:cite:`mascheroni-1797`), every Euclidean point-determination problem can be solved using **only the compass**. Straight lines cannot be continuously drawn, but any line is completely determined by two points :math:`(A, B)`.

2. **Straightedge Alone with One Fixed Circle — Jean-Victor Poncelet (1822) & Jakob Steiner (1833)**:
   Conversely, a straightedge *alone* in an empty plane can execute only projectively invariant constructions (such as harmonic conjugates and polars) and cannot solve quadratic metric problems. :person:`Jean-Victor Poncelet <poncelet>` (:cite:`poncelet-1822`) observed, and :person:`Jakob Steiner <steiner>` rigorously demonstrated in *Die geometrischen Constructionen* (:cite:`steiner-1833`), that **a single permanently drawn circle together with its center** :math:`M` (:term:`fester Hülfskreis <fester-huelfskreis>`) suffices to execute *every* ruler-and-compass construction using the straightedge alone via eight canonical problems (§ 18, ``[68]``–``[85]``) built from complete quadrangles, centers of similitude (:term:`Aehnlichkeitspunkte <aehnlichkeitspunkte>`), and radical axes (:term:`Linie der gleichen Potenzen <linie-der-gleichen-potenzen>`).

.. picture:: /_static/figures/fig_mascheroni_steiner_duality.svg

The 4-Track Codex Architecture
------------------------------

Following the GEOMETOR Digital Scriptorium canon, each section of *Die geometrischen Constructionen* is presented across four synchronized companion tracks:

- **German Primary Witness (``de``)**: Verbatim archival transcription based on the 1833 Berlin *editio princeps* (Ferdinand Dümmler) and Arthur Joachim von Oettingen's 1895 Ostwald Klassiker Nr. 60 edition, preserving original pagination in square brackets ``[1]``–``[85]``.
- **English Translation (``en``)**: Direct scholarly translation into English, integrating modern projective formulations and Lemoine's 1902 geometrographic analysis.
- **Analytical Summary (``summary``)**: Concise operational breakdown of theorems, projective configurations, operation symbols :math:`l_1 R_1 + l_2 R_2`, and complexity.
- **Commentary & Notes (``notes``)**: Historical lineage, projective foundations, Hilbert Chapter VII field hierarchies (Pythagorean vs. Euclidean quadratic closures), and why center :math:`M` cannot be omitted.

The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by :person:`phi ARCHITECT <phi-architect>`, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge:

- **Extracting Historical Semantic Knowledge**: Recovering the deductive structure of classical geometric, axiomatic, and philosophical treatises—elevating verbatim primary prose, archival scans, and calibrated ``.euclid-graphic`` diagrams into addressable semantic graphs.
- **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (SymPy) over closed-form radical fields without numerical approximations or floats.
- **Repurposing Knowledge Across Mediums**: Deploying extracted structures across multi-track **Book Codices**, interactive SVG laboratories, and computational notebooks.

Sources, Provenance & Repository Architecture
---------------------------------------------

- **Python Package**: ``src/geometor/steiner/`` (Python >= 3.13)
- **Codex Edition Track**: ``docsrc/constructionen_1833/`` (``:layout: book``)
- **Edition Structure Map**: ``resources/constructionen_1833/structure_map.json``
- **Archival PDFs & Sources**: ``resources/constructionen_1833/pdfs/`` and ``sources/``
- **Scholarly Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
- **Automated Verification**: ``tests/`` (``pytest``) and ``docsrc/`` (``publish build``)
