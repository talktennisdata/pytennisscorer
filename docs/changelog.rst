Changelog
=========

All notable changes to pytennisscorer will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Added
~~~~~
* GitHub Actions CI/CD workflows for testing, releasing, and documentation
* Comprehensive Sphinx documentation
* Support for GitHub Pages documentation hosting
* Automated PyPI publishing workflow
* Test coverage reporting to Codecov

[0.1.0] - 2024-01-01
--------------------

Initial Release

Added
~~~~~
* Core ``TennisScorer`` class for match state management
* Support for 5 different match types:

  * Singles Grand Slam (Best of 5)
  * Singles ATP Finals (Best of 3)
  * Doubles Davis Cup (Best of 3, no-ad)
  * Doubles ATP Tour (Best of 3, match tiebreak)
  * Doubles Grand Slam (Best of 3, match tiebreak at 6-6)

* Comprehensive scoring logic:

  * Standard tennis scoring (15, 30, 40, game)
  * Deuce and advantage handling
  * No-ad scoring (deciding point at deuce)
  * Standard tiebreak (first to 7, win by 2)
  * Match tiebreak (first to 10, win by 2)

* Server tracking and automatic rotation
* Complete undo functionality with state history
* Type-safe implementation with full type hints
* Zero runtime dependencies
* Comprehensive test suite with 80%+ coverage
* Property-based testing with Hypothesis
* Example Jupyter notebook

Features
~~~~~~~~
* Immutable state management using frozen dataclasses
* Functional programming approach with pure functions
* Automatic server rotation based on game/tiebreak rules
* Score formatting in standard tennis notation
* Match completion detection
* Winner determination

Developer Experience
~~~~~~~~~~~~~~~~~~~~
* Full MyPy strict mode compliance
* Ruff linting and formatting
* Comprehensive pytest test suite
* Makefile for common development tasks
* Support for Python 3.9, 3.10, 3.11, and 3.12

Documentation
~~~~~~~~~~~~~
* Complete API documentation with examples
* Quick start guide
* Match types explanation
* Contributing guidelines
* Testing documentation