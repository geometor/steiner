=======
steiner
=======

the Swiss synthetic geometer whose 1833 treatise proved that every Euclidean construction can be performed with a straightedge alone given a single fixed circle and its center

Edition Overview
----------------

- **Treatise**: *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises*
- **Author**: Jakob Steiner
- **Primary Edition Track**: ``docsrc/constructionen_1833/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   steiner --help

Links
-----

- **Documentation**: https://geometor.github.io/steiner
- **Repository**: https://github.com/geometor/steiner
- **Issues**: https://github.com/geometor/steiner/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
