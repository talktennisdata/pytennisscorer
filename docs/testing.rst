Testing
=======

pytennisscorer has a comprehensive test suite to ensure reliability and correctness.

Test Structure
--------------

The test suite is organized in the ``tests/`` directory:

.. code-block:: text

   tests/
   ├── test_scorer.py       # TennisScorer API tests
   ├── test_scoring.py      # Point scoring logic tests
   ├── test_progression.py  # Set/match progression tests
   ├── test_configs.py      # Configuration tests
   ├── test_formatter.py    # Score formatting tests
   ├── test_models.py       # Data model tests
   └── test_tiebreak.py     # Tiebreak-specific tests

Running Tests
-------------

Basic Test Execution
~~~~~~~~~~~~~~~~~~~~

Run all tests:

.. code-block:: bash

   make test

Or directly with pytest:

.. code-block:: bash

   uv run pytest

Verbose output:

.. code-block:: bash

   uv run pytest -v

Specific Tests
~~~~~~~~~~~~~~

Run a specific test file:

.. code-block:: bash

   uv run pytest tests/test_scorer.py

Run a specific test function:

.. code-block:: bash

   uv run pytest tests/test_scorer.py::test_increase_score_player_0

Run tests matching a pattern:

.. code-block:: bash

   uv run pytest -k "tiebreak"

Test Coverage
-------------

Generate Coverage Report
~~~~~~~~~~~~~~~~~~~~~~~~

Run tests with coverage:

.. code-block:: bash

   make test-cov

This generates:

* Terminal report with missing lines
* HTML report in ``htmlcov/``
* XML report for CI integration

View HTML coverage report:

.. code-block:: bash

   open htmlcov/index.html  # macOS
   xdg-open htmlcov/index.html  # Linux
   start htmlcov/index.html  # Windows

Coverage Requirements
~~~~~~~~~~~~~~~~~~~~~

* Minimum coverage: **80%**
* CI fails if coverage drops below threshold
* New code should include tests

Test Markers
------------

We use pytest markers to categorize tests:

.. code-block:: python

   @pytest.mark.unit         # Fast, isolated unit tests
   @pytest.mark.integration  # Integration tests
   @pytest.mark.slow         # Slow-running tests

Run tests by marker:

.. code-block:: bash

   # Only unit tests
   uv run pytest -m unit

   # Only integration tests
   uv run pytest -m integration

   # Exclude slow tests
   uv run pytest -m "not slow"

Writing Tests
-------------

Test Structure
~~~~~~~~~~~~~~

Follow this structure for test files:

.. code-block:: python

   import pytest
   from pytennisscorer import TennisScorer, MatchType

   class TestTennisScorer:
       """Test suite for TennisScorer class."""

       def test_initialization_singles_grand_slam(self):
           """Test scorer initialization with Grand Slam match type."""
           scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)
           assert scorer is not None

       def test_increase_score_player_0(self):
           """Test scoring a point for player 0."""
           scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)
           scorer.increase_score(0)
           score = scorer.get_score()
           assert score['game_score'] == '15-0'

Test Naming Convention
~~~~~~~~~~~~~~~~~~~~~~

Use descriptive test names:

.. code-block:: python

   # Good
   def test_tiebreak_score_reaches_seven_with_two_point_margin(self):
       pass

   # Bad
   def test_tiebreak(self):
       pass

Using Fixtures
~~~~~~~~~~~~~~

Create reusable test fixtures:

.. code-block:: python

   @pytest.fixture
   def grand_slam_scorer():
       """Fixture for Grand Slam scorer."""
       return TennisScorer(MatchType.SINGLES_GRAND_SLAM)

   def test_with_fixture(grand_slam_scorer):
       """Test using fixture."""
       grand_slam_scorer.increase_score(0)
       assert grand_slam_scorer.get_score()['game_score'] == '15-0'

Property-Based Testing
----------------------

We use Hypothesis for property-based testing:

.. code-block:: python

   from hypothesis import given, strategies as st

   @given(
       player=st.integers(min_value=0, max_value=1),
       points=st.lists(st.integers(min_value=0, max_value=1), min_size=1, max_size=100)
   )
   def test_undo_reverses_score(player, points):
       """Test that undo always reverses the last score."""
       scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

       # Score points
       for p in points:
           scorer.increase_score(p)

       initial_score = scorer.get_score()

       # Add and undo
       scorer.increase_score(player)
       scorer.undo()

       assert scorer.get_score() == initial_score

Test Best Practices
-------------------

1. **Isolation**: Tests should not depend on each other
2. **Clarity**: Test names should describe what they test
3. **Coverage**: Test edge cases and error conditions
4. **Speed**: Keep unit tests fast (< 1 second)
5. **Determinism**: Tests should produce consistent results

Common Test Scenarios
---------------------

Game Scenarios
~~~~~~~~~~~~~~

.. code-block:: python

   def test_game_to_deuce():
       """Test game reaching deuce."""
       scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

       # Score to 40-40
       for _ in range(3):
           scorer.increase_score(0)
           scorer.increase_score(1)

       score = scorer.get_score()
       assert '40-40' in score['game_score'] or 'Deuce' in score['game_score']

Tiebreak Scenarios
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_tiebreak_to_seven():
       """Test standard tiebreak to 7 points."""
       scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

       # Simulate getting to tiebreak
       # ... scoring logic ...

       # Score tiebreak points
       for _ in range(7):
           scorer.increase_score(0)

       score = scorer.get_score()
       assert not score['in_tiebreak']  # Tiebreak should be over

Match Completion
~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_match_completion():
       """Test match completion detection."""
       scorer = TennisScorer(MatchType.SINGLES_ATP_FINALS)

       # Simulate complete match
       # ... scoring logic ...

       assert scorer.is_match_complete()
       assert scorer.get_winner() in [0, 1]

Debugging Tests
---------------

Use pytest debugging options:

.. code-block:: bash

   # Drop into debugger on failure
   uv run pytest --pdb

   # Show local variables on failure
   uv run pytest -l

   # Show print statements
   uv run pytest -s

   # Maximum verbosity
   uv run pytest -vvv

Continuous Integration
----------------------

Tests run automatically on:

* Every push to main/develop branches
* Every pull request
* Multiple Python versions (3.9-3.12)
* Multiple operating systems (Linux, Windows, macOS)

CI configuration is in ``.github/workflows/ci.yml``.