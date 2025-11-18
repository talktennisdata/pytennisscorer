.. pytennisscorer documentation master file

pytennisscorer Documentation
=============================

.. image:: https://img.shields.io/pypi/v/pytennisscorer.svg
   :target: https://pypi.org/project/pytennisscorer/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pytennisscorer.svg
   :target: https://pypi.org/project/pytennisscorer/
   :alt: Python Versions

.. image:: https://github.com/seidlr/pytennisscorer/workflows/CI/badge.svg
   :target: https://github.com/seidlr/pytennisscorer/actions
   :alt: CI Status

.. image:: https://codecov.io/gh/seidlr/pytennisscorer/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/seidlr/pytennisscorer
   :alt: Coverage Status

**pytennisscorer** is a Python package for tennis match scoring with support for various match formats including singles and doubles matches, with different tiebreak and deuce rules.

Features
--------

* Support for multiple match types (Grand Slam, ATP Finals, Davis Cup, ATP Tour)
* Comprehensive handling of game scoring, deuce, and advantage
* Multiple tiebreak formats (standard, match tiebreak, deciding point)
* Server tracking and automatic rotation
* Complete match state management with undo functionality
* Type-safe implementation with full type hints
* Zero external dependencies

Installation
------------

Install pytennisscorer using pip:

.. code-block:: bash

   pip install pytennisscorer

Or using uv (recommended):

.. code-block:: bash

   uv pip install pytennisscorer

Quick Start
-----------

.. code-block:: python

   from pytennisscorer import TennisScorer, MatchType

   # Create a scorer for a Grand Slam match
   scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

   # Score some points
   scorer.increase_score(0)  # Player 0 scores
   scorer.increase_score(1)  # Player 1 scores

   # Get current score
   score = scorer.get_score()
   print(f"Set {score['current_set']+1}: {score['sets_score']}")
   print(f"Game: {score['game_score']}")
   print(f"Server: Player {score['server']}")

   # Undo last point if needed
   scorer.undo()

   # Check if match is complete
   if scorer.is_match_complete():
       winner = scorer.get_winner()
       print(f"Match winner: Player {winner}")

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   match_types
   api_reference

.. toctree::
   :maxdepth: 2
   :caption: Developer Guide

   contributing
   testing
   changelog

.. toctree::
   :maxdepth: 1
   :caption: API Documentation

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`